res=0
def sumit(root,level):
	
	if(root==null):
		return 0
	else:
		level=level+1
		i = level*root.data
		i += sumit(root.left,level)
		i += sumit(root.right,level)
	return i


sumit(node,0)
	

