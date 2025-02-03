If (5,2,3) is invoked then:
1. The recursive call to towers() will be invoked will be towers(0,1,3) where x(number of disks) =0, 
y(from destination) = 1 and z(to destination) = 3.
2. Five more recursive calls to towers() will be made before this first recursive call actually returns 
to the initial invocation.
3. Move #5 will be printed to the screen when the first recursive call returns. When all recursive calls are done, the move that is printed to the screen is Move #31.
4. Eleven more recursive calls to towers() will be invoked for the second recursive call. The second recursive call to towers() will be invoked will be towers(1,3,1) where x(number of disks) =1, 
y(from destination) = 3 and z(to destination) = 1.
If (8,1,2)  is invoked:
It can be seen that 255 lines of code will be printed to stdout when towers(8,1,2) is invoked.



This website was used to navigate on ssh and editing files:
https://help.dreamhost.com/hc/en-us/articles/115006413028-Creating-and-editing-a-file-via-SSH
