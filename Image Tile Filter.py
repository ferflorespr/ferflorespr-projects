

def copy_image(image):
  New_image=[] #cretes new list
  for i in image:#attributes variable i in every row of image
    new_img2=[]#for every i or row, create a list so that it eventually can be 2D
    for j in i: #attribute variable j to every element in rows(i)
      new_img2.append(j)#adds j to end of every list created for rows
    New_image.append(new_img2)#adds the list of evry row tp the initial list created
  return New_image#returns the copy of image created by theses for loops

def tile(image): 
  Tile_image=copy_image(image)  #copy of image


  for row_index in range(0,len(image),2):#Original code base from invert not working?
    #Think about the nested for loops four as a big square frame not list[]
    for col_index in range(0,len(image[0]),2):#increment set and fixed
     #No ifs or extra loops according to Marco, start over
     #Similar to blur: just pure math
     
      Tile_image[row_index//2][((col_index+1)//2)+len(image[0])//2]=image[row_index][col_index+1]
      Tile_image[((row_index+1)//2)+len(image)//2][((col_index+1)//2)+len(image[0])//2]=image[row_index+1][col_index+1]



      
  return Tile_image