// randomise array
function shuffleArray(array) {
   for (var i = array.length - 1; i > 0; i--) {
       // Generate random number
       var j = Math.floor(Math.random() * (i + 1));
       var temp = array[i];
       array[i] = array[j];
       array[j] = temp;
   }
   return array;
}

// reads dovnloads cards and reodered in randomise order
function shuffle_cards() {
    //const cards_map = new Map(); //  collaction name picture and 
    if (cards_array.length)  {
            switch(cards_array.length) {
              case 0:
              case 1:
                document.getElementById("message").innerHTML = "Finish the case. Select three cards";
                break;
              case 3:
                document.getElementById("shuffle_cards").innerHTML = "Please enough ...";
                break;
              default:
            }
    } else {
        let imgs = document.getElementsByClassName("img-card");
        let imgs_id = [];
        //create array of id
        for (let i = 0; i < imgs.length; i++) {
            imgs_id[i] = imgs[i].id;
        }
        imgs_id = shuffleArray(imgs_id);
        // display shuffled cards
        document.getElementById("display").replaceChildren(); // del hiden elements
        for (let i = 0; i < imgs_id.length; i++) {
            var img=document.createElement("img");
            img.setAttribute('src',`static/media/cards/title.jpg`);
            img.setAttribute('id',`${imgs_id[i]}`);
            img.setAttribute('class','img-card');
            img.setAttribute('style','width:150px;');
            img.setAttribute('onclick','reply_click(this.id)');
            var foo = document.getElementById("display");
            foo.appendChild(img);
        }
        document.getElementById("message").innerHTML = "Сome up with a question and Select three cards<br><small>Придумайте запитання та виберіть три картки</small>";
    }
}



// perform select 3 cardsand dislay them
function reply_click(clicked_id) {
     if (cards_array.length < 3) {
         cards_array.push(clicked_id);  // Adds a new element 
         document.getElementById(clicked_id).style = `display: none ;`;
         var img_selected=document.createElement("img");
         img_selected.src=`static/media/cards/title_sel.jpg`
         img_selected.class=`img-card`
         img_selected.style=`width:150px;`
         document.getElementById(clicked_id).replaceWith(img_selected);
         // show sequence_number - button
         document.getElementById("sequence_number").style = `
             border: 2px solid red; 
             border-radius: 20px; 
             padding: 19px; 
             width:50px; 
             text-align: center;
             font-style: italic;
             text-decoration-style: solid;
             font-size: 18px; 
             position: fixed;
             top: 10px;
             left: 10px; 
             box-shadow: 10px 10px;
             background-color: red;
             z-index: 1;
         `;
         document.getElementById("sequence_number").innerHTML = cards_array.length + " in 3";
         //alert(clicked_id);
     } 
     if (cards_array.length == 3)  {
        setTimeout(function(){
            document.getElementById("sequence_number").style = `display: none ;`;

            document.getElementById("message").innerHTML = "You have selected the following cards";
              //document.getElementById("display").style = `display: none ;`;
            document.getElementById("display").replaceChildren();
              //greeting = alert(cards_array);
                  //dynamically add an image and set its attribute
            for (let i = 0; i < cards_array.length; i++) {
                var img=document.createElement("img");
                img.src=`static/media/${cards_array[i]}`
                img.id=`${cards_array[i]}`
                img.class=`img-card`
                img.style=`width:150px;`
                var foo = document.getElementById("display");
                foo.appendChild(img);
            }
            // add button to have result
            var result_button=document.createElement("button");
            result_button.setAttribute('class',`button`);
            result_button.setAttribute('type',`button`);
            result_button.setAttribute('id',`meaning`);
            result_button.textContent = "Want to know the result? Хочете взнати результат?";
            //result.setAttribute('onclick','result_meaning(cards_array)');
            var foo = document.getElementById("div_meaning");
            document.getElementById("div_meaning").replaceChildren(); // del hiden elements
            foo.appendChild(result_button);
        }, 1000);

     } 
 }



const cards_array = [];
