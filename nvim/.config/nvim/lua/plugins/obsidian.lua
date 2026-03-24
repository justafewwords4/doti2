return {
  "epwalsh/obsidian.nvim",
  version = "*", -- recommended, use latest release instead of latest commit
  lazy = false,
  ft = "markdown",
  -- Replace the above line with this if you only want to load obsidian.nvim for markdown files in your vault:
  -- event = {
  --   -- If you want to use the home shortcut '~' here you need to call 'vim.fn.expand'.
  --   -- E.g. "BufReadPre " .. vim.fn.expand "~" .. "/my-vault/*.md"
  --   -- refer to `:h file-pattern` for more examples
  --   "BufReadPre path/to/my-vault/*.md",
  --   "BufNewFile path/to/my-vault/*.md",
  -- },
  dependencies = {
    -- Required.
    "nvim-lua/plenary.nvim",

    -- see below for full list of optional dependencies 👇
  },
  opts = {
    workspaces = {
      {
        name = "cerebras",
        path = "~/zettelkasten",
        overrides = {
          notes_subdir = "notes",
        },
      },
    },

    ui = { enable = false }, -- por compatibilidad con render-markdown.nvim

    -- see below for full list of options 👇
    vim.keymap.set("n", "<leader>on", "<cmd>ObsidianNew<CR>"),
    vim.keymap.set("n", "<leader>or", "<cmd>ObsidianRename<CR>"),
    vim.keymap.set("n", "<leader>oy", "<cmd>ObsidianYesterday<CR>"),
    vim.keymap.set("n", "<leader>ot", "<cmd>ObsidianToday<CR>"),
    vim.keymap.set("n", "<leader>oT", "<cmd>ObsidianTomorrow<CR>"),
    vim.keymap.set("n", "<leader>os", "<cmd>ObsidianSearch<CR>"),
    vim.keymap.set("n", "<A-t>", "<cmd>ObsidianToggleCheckbox<CR>"),
    vim.keymap.set("i", "<A-t>", "<Esc><cmd>ObsidianToggleCheckbox<CR>"),
  },
}
