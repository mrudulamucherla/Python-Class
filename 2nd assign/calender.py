# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:01:20 2020

@author: mrudula
"""
#windows and students program
window =list(range(0,1000))
 for x in range(0,1000):
      window[x]=0 #all windows are closed initially
      #range1=list(range(0,1000))
      s=0
      w=0
      for s in range(1,1001):
          for w in range(1,1001):
              if w%s==0:
                  if window[w-1]==0:
                      window[w-1]=1
                      else:
                          window[w-1]=0
                          else:
                              pass
                          
                            
                            
                            
                            count=0
                            print("open windows are")
                            for i in range(0,1000):
                                if window[i]==1:
                                    count=count+1
                                    print(i+1)
                                    print("total number of windows open are",count)
      
    