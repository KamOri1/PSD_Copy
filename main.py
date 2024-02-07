from copy_psd import CopyPSD


but1 = CopyPSD()
but1.open_window()
but1.button_open_file_function("Open file", but1.open_file_function, 0.838, 0.3,  'white', '#283593','#689F38',)
but1.button_open_file_function("Copy file", but1.copy_psd_18x, 0.838, 0.5,  'white', '#283593','#689F38')
but1.button_open_file_function("Exit", but1.close, 0.838, 0.6, 'white', '#CC0033','#FF0033')
but1.button_open_file_function("Create folder", but1.folder_create, 0.838, 0.4,  'white', '#283593', '#689F38')
but1.foto()

but1.start_loop()