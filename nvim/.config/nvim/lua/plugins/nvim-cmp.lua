-- if true then
--   return {}
-- end

return {
  -- override nvim-cmp and add cmp-emoji
  {
    "hrsh7th/nvim-cmp",
    lazy = false,
    dependencies = { "hrsh7th/cmp-emoji", "obsidian-nvim/obsidian.nvim" },
    ---@param opts cmp.ConfigSchema
    opts = function(_, opts)
      table.insert(opts.sources, { name = "emoji" })
      table.insert(opts.sources, { name = "obsidian" })
    end,
  },
}
