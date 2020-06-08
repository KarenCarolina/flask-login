prev=document.getElementById("previous");
next=document.getElementById("next");
slide=document.querySelector(".slide");
slide1=document.getElementById("slider1");
slide2=document.getElementById("slider2");
slide3=document.getElementById("slider3");
let images=[slide1,slide2,slide3];
var indice=0;
slide.addEventListener("mouseover",function(){
    // alert("hello");
    prev.style.display="block";
    next.style.display="block"; 
})

slide.addEventListener("mouseout",function(){
    // alert("hello");
    prev.style.display="none";
    next.style.display="none"; 
})

next.addEventListener("click",function(){
        
    if(indice<images.length-1){
    
        indice++;
        // console.log(indice+"n");
        
    }else{
        indice=0;
    }

    for (let index = 0; index < images.length; index++) {

        if(indice==index){
            images[index].style.display="block";
        }else{
            images[index].style.display="none";
        }        
    }
})


prev.addEventListener("click",function(){

    if(indice>0){
        indice--;
        // console.log(indice);
        

    }else{ 
        indice=images.length-1; 
    }

    for (let index = 0; index < images.length; index++) {
        if(indice==index){
            images[index].style.display="block";
        }else{
            images[index].style.display="none";
        }            
    }

})
