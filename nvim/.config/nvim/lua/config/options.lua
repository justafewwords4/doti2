-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

local opt = vim.opt
opt.wrap = true
opt.linebreak = true

opt.textwidth = 80

-- For init.lua (Lua)
opt.spell = true -- Enable spellchecking
opt.spelllang = "en,es" -- Add Spanish (es) alongside English (en)
-- Or for just Spanish: vim.opt.spelllang = 'es'
-- local vim = vim
-- vim.g.loaded_netrw = 1
-- vim.g.loaded_netrwPlugin = 1
