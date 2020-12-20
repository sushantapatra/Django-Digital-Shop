function init(){
    //alert('window load');
}


function changeImage(event){
    var mainImage=document.getElementById('main_img');
    mainImage.src=event.target.src;
}


window.onload=init;