## Tags mais usadas

[TailwindCss Docs](https://tailwindcss.com/docs/installation)

### Background-color [-> Link-docs](https://tailwindcss.com/docs/background-color)
``` console
bg-white
bg-black
bg-green-100
bg-blue-500/50      #50%
bg-gray-800
bg-[#181818]
```
```html 
<!-- example -->
<div class="bg-black">contents..</div>
```

### Text-color [-> Link-docs](https://tailwindcss.com/docs/text-color)
``` console
text-white
text-black
text-yellow-100
text-purple-500/75      #75%
text-gray-900
text-[#181818]
```
```html 
<!-- example -->
<p class="text-black">contents..</p>
```

### Font-size [-> Link-docs](https://tailwindcss.com/docs/font-size)
``` console
text-xs     #12px
text-sm     #14px
text-base   #16px
text-lg     #18px
```
```html 
<!-- example -->
<p class="text-xs">contents..</p>
```

### Padding [-> Link-docs](https://tailwindcss.com/docs/padding)
``` console
p-0     #0px
p-1     #bottom:4px, top:4px, left:4px, right:4px
py-1    #bottom:4px, top:4px
px-1    #left:4px, right:4px
```
```html 
<!-- example -->
<span class="p-1">contents..</span>
```

### Margin [-> Link-docs](https://tailwindcss.com/docs/margin)
``` console
m-0     #0px
m-1     #bottom:4px, top:4px, left:4px, right:4px
my-1    #bottom:4px, top:4px
mx-1    #left:4px, right:4px
mb-1 | mt-1 | ml-1 | mr-1   #bottom:4px, top:4px, left:4px, right:4px   
```
```html 
<!-- example -->
<div class="m-1">contents..</div>
```

### Width [-> Link-docs](https://tailwindcss.com/docs/width)
``` console
w-0     #0px
w-px    #1px
w-9.5   #2px
w-1     #4px
w-96    #384px
w-2/4   #50%
w-full  #100%
w-auto  #auto-content..
```
```html 
<!-- example -->
<div class="w-96">
    <span class="w-full">contents..</span>
</div>
```

### Height [-> Link-docs](https://tailwindcss.com/docs/height)
``` console
h-0     #0px
h-px    #1px
h-9.5   #2px
h-1     #4px
h-96    #384px
h-2/4   #50%
h-full  #100%
h-auto  #auto-content..
```
```html 
<!-- example -->
<div class="w-96 h-96">
    <span class="w-full h-auto">contents..</span>
</div>
```

### Display [-> Link-docs](https://tailwindcss.com/docs/display)
```console
block                   #display: block
inline-block	        #display: inline-block
inline	                #display: inline
flex	                #display: flex
inline-flex	            #display: inline-flex
grid	                #display: grid
hidden	                #display: none
```
```html 
<!-- example -->
<div class="flex">
    <span class="inline-flex">contents..</span>
    <span class="inline-flex">contents..</span>
    <!-- <p class="hidden">contents..</p> -->
</div>
```