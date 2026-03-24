-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
local map = LazyVim.safe_keymap_set
map("n", "ss", ":w<cr>", { desc = "Split Vertically" })
map("n", "sv", "<C-w>v", { desc = "Split Vertically" })
map("n", "so", "<C-w>s", { desc = "Split Horizontally" })
map("n", "sl", "<C-w>l", { desc = "Go to right panel" })
map("n", "sh", "<C-w>h", { desc = "Go to left panel" })
map("n", "sj", "<C-w>j", { desc = "Go to bottom panel" })
map("n", "sk", "<C-w>k", { desc = "Go to upper panel" })
map("n", "sd", ":bdelete<cr>", { desc = "Go to upper panel" })
map("v", "gq", "gq", { desc = "Format Text" })
map("n", "<Leader>h", "<cmd>HopChar1<cr>", { desc = "Hop 1 char" })
map("n", "<c-t>", "<cmd>ToggleTerm<cr>", { desc = "Desplegar Terminal" })
-- map("n", "<Leader>e", "<cmd>Neotree position=right<cr>", { desc = "Neotree" })
map("t", "<c-t>", "<cmd>ToggleTerm<cr>", { desc = "Desplegar Terminal" })

-- Custom keymap: Insert Markdown H2 with current time on a new line
map("n", "<M-d>", function()
  local current_time = vim.fn.strftime("## %H:%M")
  vim.cmd("normal! o" .. current_time)
end, { desc = "Insert Markdown H2 with current time" })
