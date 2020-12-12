def install(modules):
    '''
    Allows you to download by pip all the necessary modules. A list with strings is feed into the function.
    \n.install(moduls=list)
    '''

    from pip import main

    main(["install", *modules])