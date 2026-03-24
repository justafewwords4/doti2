local auto_capitalize_group = vim.api.nvim_create_augroup("auto_capitalize", { clear = true })

vim.api.nvim_create_autocmd("InsertCharPre", {
  group = auto_capitalize_group,
  pattern = { "*.txt", "*.md" },
  callback = function()
    local char = vim.v.char
    if not char or not char:match("%a") then
      return
    end

    local line = vim.api.nvim_get_current_line()
    local col = vim.api.nvim_win_get_cursor(0)[2]
    local current_line_num = vim.fn.line(".")

    -- Capitalize at the beginning of the file
    if current_line_num == 1 and col == 0 then
      vim.v.char = char:upper()
      return
    end

    -- Capitalize at the beginning of a new paragraph
    if current_line_num > 1 then
      local prev_line = vim.api.nvim_buf_get_lines(0, current_line_num - 2, current_line_num - 1, false)[1]
      -- Check if previous line is blank (contains only whitespace)
      if prev_line and prev_line:match("^%s*$") then
        -- Check if we are at the start of the line (ignoring leading whitespace)
        if line:sub(1, col):match("^%s*$") then
          vim.v.char = char:upper()
          return
        end
      end
    end

    if col > 0 then
      local last_2_bytes = line:sub(col - 1, col)
      local last_1_byte = line:sub(col, col)

      -- Caso: Directamente después de ¿ o ¡
      if last_2_bytes == "¿" or last_2_bytes == "¡" then
        vim.v.char = char:upper()
        return
      end

      -- Caso: Después de puntuación (incluyendo ']') y un espacio
      if last_1_byte == " " and col >= 2 then
        local char_before_space = line:sub(col - 1, col - 1)
        -- Añadimos ']' al grupo de coincidencia
        if char_before_space:match("[%]#.!%?%-]") then
          vim.v.char = char:upper()
          return
        end
      end
    end
  end,
})
