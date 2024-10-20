from django.shortcuts import render
from django.http import HttpResponse

def viewport(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
    .grid-container{
    /* height: 100vh; */
    display: grid;
    grid-template-columns: 40px 40px 40px 40px;
    /* grid-template-rows: 40px 40px 40px; */
    gap: 10px;
    justify-content: center;
    /* align-content: center; */
}
.grid-container div{
    background-color: tomato;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    border-radius: 50%;
}
.btn10{
    background-color: greenyellow !important;
}




.b1{
    /* grid-row-start: 2;
    grid-row-end: 4; */
}

.container{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}
.container div{
    flex: 15%;
    background-color: blueviolet;
    height: 100px;
}

@media screen and (max-width: 500px) {
    body{
        background-color: red;
    }
    .container div{
        flex: 33%;
    }
}
    </style>
  </head>
  <body>


    <!-- <div class="grid-container">

      <div>1</div>
      <div>2</div>
      <div>3</div>
      <div>4</div>
      <div>5</div>
      <div>6</div>
      <div>7</div>
      <div>8</div>
      <div>9</div>
      <div class="btn10">10</div>
    </div> -->


    <!-- <div class="dropdown">
      <p>Drop</p>
      <h2>Dropdown hide</h2>
    </div> -->
   

    <div class="container">

      <div class="item">1</div>
      <div class="item">2</div>
      <div class="item">3</div>
      <div class="item">4</div>
      <div class="item">5</div>
      <div class="item">6</div>

    </div>
  </body>
</html>
    """)
def click(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
    *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

 .my-class{
    height: 300px;
    background-color: burlywood;
    gap: 20px;
    padding: 10px;
    
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column-reverse;
} 
/* 
flex-direction:
row - horizontal 
row-reverse -> teskari horizontal
column -> vertical
column-reverse -> teskari vertical
*/


/* justify-content:
elementning ichidagi boshqa elementlarni horizontal joylashtirish
*/

/* align-items:
elementning ichidagi boshqa elementlarni vertical joylashtirish
*/
    </style>
  </head>
  <body>
    <div class="my-class">
        <h4>Logo</h4>
        <div>
            <a href="">Home</a>
            <a href="">About</a>
        </div>
        <button>Login</button>
    </div> 

    <div class="calculator">
      
        <div class="qator">
            <button>7</button>
            <button>8</button>
            <button>9</button>
            <button>-</button>
        </div>
        <div class="qator">
            <button>4</button>
            <button>5</button>
            <button>6</button>
            <button>+</button>
        </div>
        <div class="qator">
            <button>1</button>
            <button>2</button>
            <button>3</button>
            <button>*</button>
        </div>

    </div>
  </body>
</html>
    """)

def index(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
    button{
    box-shadow: 10px 0px 4px rgb(253, 4, 4);
}

p{
    text-transform: uppercase ;
    line-height: 2;
}

/* uppercase - katta 
   lowercase - kichik
   capitalize- bosh harf qilib boshlaydi
   line - height -> textlar qatori orasida masofa
*/

.position{
    height: 2000px;
    position: relative;
}

/* Fixed - ekranga yopishib qoladi */
.fixed{
    position: fixed;
    background-color: red;
}

/* Bodyda - istalgan joyga joylashadi */
.absolute{
    position: absolute;
    right: 20px;
    bottom: 40px;
    background-color: blue;
}

/* Qaysidir joyga borsa qotib qoladi */
.sticky{
    position: sticky;
    top: 0;
    background-color: yellow;
}

/* 
Positionlar bilan odatda

top, left, right, bottom - css codelar ishlatiladi
*/
    </style>
</head>
<body>
    
    <!-- <button>Hello</button> -->

    <!-- <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus velit illo dignissimos pariatur vel labore excepturi quo distinctio accusantium rem sit odit quisquam optio, possimus saepe similique odio deserunt enim?</p> -->

    <div class="position">

        <p class="fixed">Fixed</p>
        <p class="absolute">Absolute</p>

        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam assumenda iusto velit perferendis aut, sed animi dolores adipisci quaerat nobis?</p>
        <p class="sticky">Sticky</p>
        
    </div>



</body>
</html>
    """)

def login(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
    body{
  display: flex;
  flex-direction: column;
  gap: 20px;
}
input[type="text"] {
  /* background-color: blueviolet; */
  outline: none;
  padding: 10px;
  background-color: rgb(232, 163, 114);
  border: none;
}

input[name="job"]{
    /* background-color: #ff0000; */
}

input::placeholder{
    /* color: gray; */
}



img[data-name="my-image"] {
  background-color: aquamarine;
}

/* Atributning boshlanish qiymati */
[class|="mytext"] {
  color: blue;
  background-color: aqua;
}

/* Atributning oxirgi qiymatini*/
[name$="leon"] {
  color: yellow;
}

/* Atributda mavjud bolgan qiymatni */
[name*="adam"] {
  color: blueviolet;
}


:root{
    --javohir: 20px;
    --bgColor: rgb(63, 250, 1);
    --pd10: 10px;
    --fs20: 20px;
    --colorRed: #ff0000;
}
p {
  font-size: var(--fs20);
  color: var(--bgColor);
  /* background-color: var(--colorRed); */
}

p:hover{
  color: var(--colorRed);
}
h2 {
  color: var(--bgColor);
  padding: var(--pd10);
}
button {
  color: var(--bgColor);
  font-size: var(--font-big);
}

/* Mishka ustiga olib borilganda */
button:hover{
    background-color: blue;
}
/* Linkga kirilganda */
a:visited{
    color: aqua;
}
/* Inputni tanlab bosilganda */
input:focus{
    background-color: red;
   
}
/* Check qilinganda */
[type="checkbox"]:checked{
    width: 50px;
    height: 50px;
}


.clock{
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 2px solid black;
    position: relative;
    background: url(./time.gif);
    background-size: cover;
}

.clock > div{
  background-color: black;
  position: absolute;
  top: 50%;
  left: 50%;
  transform-origin: left;
  animation-iteration-count: infinite;

}
.second{
    width: 80px;
    height: 2px;    
    animation: clock 60s linear;
    box-shadow: -4px -4px 8px black;
}

.minute{
  width: 60px;
  height: 4px;
  background-color: #ff0000 !important;
  animation: clock 3600s linear;
}
.hour{
  width: 50px;
  height: 4px;
  background-color: blueviolet !important; 
  animation: clock 43200s linear;
}


@keyframes clock{
    0%{
        transform: rotateZ(-90deg);
    }
    100%{
        transform: rotateZ(270deg);
    }
}
    </style>
  </head>

  <body class="asos">
   
    <input type="text" placeholder="Name" />
    <input type="text" placeholder="Last name" />
    <br>
    <input type="number" placeholder="Age" />
    <input name="job" type="text" placeholder="Job" />
    <input type="button" value="" />

    <input type="time" name="" id="" />

    <p class="mytext-hello-blahblah">Hello world</p>

    <h2 name="john adam jack leon">Helloo</h2>

    <p>Text1</p>

    <h2>Text2</h2>

    <button>Hello</button>








    <a href="https://www.npmjs.com/" target="_blank">NPMJS</a>

    <input type="text" name="" id="" />

    <input type="checkbox" name="" id="" />

    
    
    <div class="clock">
      <div class="second"></div>
      <div class="minute"></div>
      <div class="hour"></div>
    </div>



  </body>
</html>
    ''')
def button(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <style>
    div p{
    color: red;
}

div > p{
    background-color: blue;
}

div + p{
    font-size: 30px;
    color: yellow;
}
.q1 + .q2 {
    background-color: blueviolet;
}
p + .q1 {
    background-color: aqua;
}
h2 ~ button{
    background-color: tomato;
}

button:nth-child(2n+1){
    background-color: red;
}</style>
  </head>
  <body>

    <div>
      <p>Hello</p>
      <button>
        <p>Hello nesting</p>
      </button>
      <div>
        <a href="">
          <span>
            <p>Chevara</p>
          </span>
        </a>
      </div>
    </div>
    
    <p>Qo'shni</p>
    <button>Click top</button>
    <div class="q1" >
      <h4>Hello qo'shni 1</h4>
      <h4>Hello uy 1</h4>
    </div>
    <div class="q2">
      <h4>Hello qo'shni 2</h4>
    </div>
    <div class="q2">
      <h4>Hello qo'shni 2</h4>
    </div>

    <div class="javohir">

      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
      <button>Click</button>
    
    </div>

    <button>Click bottom</button>


  </body>

  <!-- <script src="./main.js"></script> -->
</html>
    """)

def main(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- 1-div -->
    <div style="background-color: #B5CB99; padding: 100px 0px; " >
       <center >
           <h1>HELLO, THIS IS MY WEBSITE!</h1>
        </center>
    </div>

    <!-- 2-div -->
    <div style="background-color: cadetblue; padding: 20px; " >
        <!-- Navigation -->
        <center>
            <a href="">Home</a>
            <a href="">Info</a>
            <a href="">Contact</a>
            <a href="">Hubpages</a>
        </center>

        <!-- Textlar -->
        <div>
            <h2>This is header text.</h2>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis, aliquam!</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis, aliquam!</p>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis, aliquam!</p>
        </div>

    </div>

</body>
</html>
    """)

def second(request):
    return HttpResponse("""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <form action="">
      <div>
        <label for="name">Full Name</label>
        <input
        placeholder="Bu yerga matn yoziladi"
        type="text"
        name="My box"
        id="name"
        />
      </div>
      <input type="password" name="" id="">
      <br>



      <input type="checkbox" name="a" id="uzbek" />
      <label for="uzbek">Uzbek tili</label>
      <br />
      <input type="checkbox" name="a" id="english" />
      <label for="english">English</label>
      <br />
      <input type="checkbox" name="a" id="rus" />
      <label for="rus">Russian</label>
      
      <br />
      <input type="radio" name="a" id="" />

    </form>

    <button>
      Click me
    </button>


    <select name=""  id="">
      <option value="apple">Apple</option>
      <option value="samsung">Samsung</option>
      <option value="mi">Mi</option>
      <option value="sony">Sony</option>
    </select>

    <textarea name="" id="" cols="30" rows="10" style="resize: none;" >
      
    </textarea>


  </body>
</html>
    """)
# Create your views here.
