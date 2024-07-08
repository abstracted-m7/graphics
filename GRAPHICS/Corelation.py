x=np.array([1,2,3,4,5])
y=np.array([6,7,8,9,10])

def corelation(x,y):
  if len(x)==len(y):
    sum_xy=sum((x-x.mean())*(y-y.mean()))
    sum_x_squard=sum((x-x.mean())**2)
    sum_y_squard=sum((y-y.mean())**2)
    corr=sum_xy/np.sqrt(sum_x_squard*sum_y_squard)
    return corr
print(corelation(x,y))
print(corelation(x,x))

