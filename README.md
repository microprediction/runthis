# runthis ![tests](https://github.com/microprediction/runthis/workflows/tests/badge.svg) ![deploy-pypi](https://github.com/microprediction/runthis/workflows/deploy-pypi/badge.svg)

Trivial utility to help you arrange experiments like this: 

![](https://github.com/microprediction/runthis/blob/main/images/directory.png)



Don't want to do that? Thanks for stopping by anyway. 


### Cut and Paste
Use this as the main stub in your experimental files


        if __name__=='__main__':
            import os
            kwargs = parse_kwargs(__file__.split(os.path.sep)[-1])
            my_experiment(**kwargs)



See [example](https://github.com/microprediction/runthis/blob/main/examples/mean_info_max_shgo%3Fn%3D5%26d%3Dcat%26init%3D%5B0.2%2C0.2%2C0.2%5D.py)

![](https://github.com/microprediction/runthis/blob/main/images/run_this.png)


New experiment? Make a copy of the file and edit the name *only*. 


### Int, Float arguments
Just call the experiment file 

       my_function?n=int:5&d=cat&init=[float:0.2,float:0.2,float:0.2].py




### Example 

