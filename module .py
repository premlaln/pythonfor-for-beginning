#!/usr/bin/env python
# coding: utf-8

# In[6]:


from pip._vendor.colorama import init, Fore

def display(message, is_warning):
    if is_warning:
        print(Fore.Blue+message)
    else:
        print(Fore.Red+message)


# In[ ]:





# In[ ]:




