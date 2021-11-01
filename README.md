# runthis
Mini-package to make it trivial to track experiments

### Usage
Name your experiment files 

     my_function?n=5&d=cat&init=[0.2,0.2,0.2]).py
    
Then your experiment file looks like this: 

    if __name__=='__main__':
        import os
        from runthis import parse_filename
        this_file = __file__.split(os.path.sep)[-1]
        func, kwargs = parse_filename(this_file)
        do_something(**kwargs)
        
This way what you do in the experiment never gets out of sync with the code. 
   