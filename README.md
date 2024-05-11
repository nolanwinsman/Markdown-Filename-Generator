# Markdown-Filename-Generator
Python script to create a filelist table for a project in markdown. I got frustrated with having to type this out constantly so I created this script to 
generate the basic table.

## Installation

### Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x (with pip)

1. Clone the repo
```sh
git clone https://github.com/nolanwinsman/Markdown-Filename-Generator
```

## Getting Started

```sh
python main.py [directory] [--output output_file] [--verbose] [--ignore-ext ext1 ext2 ...] [--ignore-dirs dir1 dir2 ...]
```

After running the script, you should see `file_list.md` this is the output file showing you the table you can copy to your `README.md` file

## Example Output

This is the filelist this script output for me neovim config repo []()

| Filename                            | Description                         |
| ----------------------------------- | ----------------------------------- |
| init.lua                            |                                     |
| lua\keybinds.lua                    |                                     |
| lua\settings.lua                    |                                     |
| lua\bufferline-config\init.lua      |                                     |
| lua\lsp-config\language-servers.lua |                                     |
| lua\lsp-config\null-ls.lua          |                                     |
| lua\lsp-config\nvim-cmp.lua         |                                     |
| lua\lualine-config\init.lua         |                                     |
| lua\mason-config\init.lua           |                                     |
| lua\null-ls-config\init.lua         |                                     |
| lua\plugins\alpha-nvim.lua          |                                     |
| lua\plugins\bufferline.lua          |                                     |
| lua\plugins\fzf-lua.lua             |                                     |
| lua\plugins\init.lua                |                                     |
| lua\plugins\null-ls.lua             |                                     |
| lua\plugins\project.lua             |                                     |
| lua\plugins\telescope.lua           |                                     |
| lua\plugins\treesitter.lua          |                                     |
| lua\treesitter-config\init.lua      |                                     |

## Actual Filelist for This Project

| Filename     | Description                                                                       |
| ------------ | --------------------------------------------------------------------------------- |
| .gitignore   | Specifies intentionally untracked files to ignore. Currently just `file_list.md`  |
| LICENSE      | Contains permissions and limitations for use of code                              |
| README.md    | This file                                                                         |
| file_list.md | Output of the script. Not stored in repo                                          |
| main.py      | Python script for generating a Markdown file list table.                          |

# Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/Markdown-Filename-Generator](https://github.com/nolanwinsman/Markdown-Filename-Generator)

# Contributers
- nolanwinsman