# runthis
Tired of your experiments becoming a mess? Me too. I finally adopted the policy of making all my experiment files the same, and changing only the name of the file. 

### Examples
See [examples](https://github.com/microprediction/runthis/blob/main/examples/mean_info_max_shgo%3Fn%3D5%26d%3Dcat%26init%3D%5B0.2%2C0.2%2C0.2%5D.py)

### Usage
Name your experiment files like this: 

     my_function?n=5&d=cat&init=[0.2,0.2,0.2].py
    
Then your experiment file looks like this: 

    if __name__=='__main__':
        import os
        from runthis import parse_filename
        this_file = __file__.split(os.path.sep)[-1]
        func, kwargs = parse_filename(this_file)
        do_something(**kwargs)
        
This way what you do in the experiment never gets out of sync with the code. 
   
