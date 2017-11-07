if !has('python')
	finish
endif

let $vimdir="~/.vim/plugin/depdiff/"

vnoremap <silent> <F5> :<C-U>PASTE<CR>

function! DepDiff()
	pyfile $vimdir/depdiff.py
endfunc

command! DEPDIFF call DepDiff()
