let noOfCharac = 50;
let paras = document.querySelectorAll("p.para");
paras.forEach(para => {
    //If text length is less that noOfCharac... then hide the read more button
    if(para.textContent.length < noOfCharac){
        para.nextElementSibling.style.display = "none";
    }
    else{
        let displayText = para.textContent.slice(0,noOfCharac);
        let moreText = para.textContent.slice(noOfCharac);
        para.innerHTML = `${displayText}<span class="dots">...</span><span class="hide more">${moreText}</span>`;
    }
});

// function readMore(btn){
//     let post = btn.parentElement;
//     post.querySelector(".dots").classList.toggle("hide");
//     post.querySelector(".more").classList.toggle("hide");
//     btn.textContent == "Read More" ? btn.textContent = "Read Less" : btn.textContent = "Read More";
// }