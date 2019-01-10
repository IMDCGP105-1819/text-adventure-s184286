var seeletter1=0
var gotletter1=0
var gotpaper=0
var didhelp=0
var gothanky=0
var didpee=0
var didkill=0
var didhelpridge=0
var gotcrumpled=0

function hospitalinput(HospitalActions) {
      if (HospitalActions.options[HospitalActions.selectedIndex].text == "get") {
          var answer=prompt("What would you like me to get?","")
          var answerlow=answer.toLowerCase()
          if ((answerlow.indexOf("paper")!= -1 || answerlow.indexOf("writ")!=-1 || answerlow.indexOf("crump")!=-1) && gotcrumpled==0) {
               gotcrumpled=1 
               alert("In curiosity I walk over and pick up the crumpled paper.  I smooth it out with my hands.")
          }
          
          else {
               alert("My action has no effect.")
               }
        } 
      else if (HospitalActions.options[HospitalActions.selectedIndex].text=="read") {
               if (gotcrumpled==1) {
                    window.location.replace("flanders.htm")
               }
               else {
                    var answer=prompt("What would you like me to read?","")
                    var answerlow=answer.toLowerCase()
                    alert("My action has no effect.")
               }
      } 
     }

function ridgeinput(RidgeActions) {
     if (RidgeActions.options[RidgeActions.selectedIndex].text == "shoot"){
                   
               if (didkill==0) {
                    didkill=1
                    alert("I fire once.  The German falls.  He wriggles on the ground.  I let out an incoherent yell. I run toward him.  I fire again, and again.  The wriggling stops.")
               }
               else  {
                    
                    alert("My action has no effect.  'Arthur, let's go!' cries Alex.")
               }
     }         
     else if (RidgeActions.options[RidgeActions.selectedIndex].text == "help"){
               if (didkill==1 && didhelpridge==0) {
                    didhelpridge=1
                    alert("I grab Arthur and throw him over my shoulder.  He grunts in pain.  I look at George.  Alex's promise must be broken.")
               }
               else if (didhelpridge==1){
                    alert("My action has no effect.  'Arthur, let's go!' cries Alex")
               }
               else {
                    alert("'Arthur, the German!' cries Alex.")
               }
      }
      else if (RidgeActions.options[RidgeActions.selectedIndex].text == "go"){
               if (didhelpridge==1 && didkill==1) {
                    window.location.replace("letter6.htm")
               }
               else {
                    alert("'Arthur!... ArthurI...Don't leave me!' cries Alex.")          
               }
      }  
      else {
               alert("My action has no effect.")
               }

}


function trenchinput(TrenchActions) {
     if (TrenchActions.options[TrenchActions.selectedIndex].text == "get"){
          var answer=prompt("What would you like me to get?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("handk")!=-1 && gothanky!=1) {
               gothanky=1
               alert("Fighting pain and fatigue I fumble in desperate search of something to cover my face. Finally, my fingers find my handkerchief tucked inside a front pocket.")
          }
          else if (gothanky!=1) {
               alert("My action has no effect.  The vapour thickens.  I gasp desperately for breath. I must find something to cover my face I think to myself.")
          }
          else {
               alert("My action has no effect.")
          }
       }         
     else if (TrenchActions.options[TrenchActions.selectedIndex].text == "urinate"){
          var answer=prompt("What would you like me to urinate on?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("handk")!=-1 && gothanky==1) {
               didpee=1
               alert("I soak the handkerchief. I cough uncontrollably in a desperate attempt to clear my lungs.")
          }
          else if (answerlow.indexOf("handk")!=-1){
               alert("My action has no effect.  I gasp desperately for breath.  I must find that handkerchief first I think to myself.")          
               }
          else {
               alert("My action has no effect.  I gasp desperately for breath.  I must find something wet to cover my face I think to myself.")
               }
     }
      else if (TrenchActions.options[TrenchActions.selectedIndex].text == "wear"){
          var answer=prompt("What would you like me to wear?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("handk")!=-1 && gothanky==1 && didpee==1) {
               window.location.replace("letter4.htm")
          }
          else if (answerlow.indexOf("handk")!=-1 && gothanky==1){
               gothanky=0
               alert("I place the handkerchief over my face, but to no effect.  The vapour fills my lungs at each gasp. I cannot suppress the urge to rip the handkerchief from my face, and so I do.")          
               }
          else {
               alert("My action has no effect.  I gasp desperately for breath.  I must find something wet to cover my face I think to myself.")
               }
     }
}

function plaininput(PlainActions) {
      if (PlainActions.options[PlainActions.selectedIndex].text == "get") {
          var answer=prompt("What would you like me to get?","")
          var answerlow=answer.toLowerCase()
          if ((answerlow.indexOf("shimm")!= -1 || answerlow.indexOf("some")!=-1) && didhelp==1) {
               window.location.replace("letter3.htm")
          }
          
          else {
               alert("My action has no effect.  'For Christ's sake help me Arthur!' pleads George.")
               }
        } 
      else if (PlainActions.options[PlainActions.selectedIndex].text=="help") {
               didhelp=1               
               alert("I grab Alex's left arm; George grabs the right.  We sling Alex's arms behind our necks and begin to drag his limp body along.  For whatever reason I take occasion to glance back and notice something shimmer in the dim light.")
      } 
     }
function homeinput(HomeActions) {

     if (HomeActions.options[HomeActions.selectedIndex].text == "get") {
          var answer=prompt("What would you like me to get?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("paper")!=-1) {
               gotpaper=1
               alert("The paper is creased down the middle.  I unfold it and stare at the black print.  The mass of varied size symbols makes no sense to me.")
          }
          else {
               alert("My action has no effect.  'The paper's on the hutch,' repeats the woman.")
               }
     }    
     else if (HomeActions.options[HomeActions.selectedIndex].text=="ask") {
          var answer=prompt("Who would you like to ask: Alex, Benny, or the woman?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("alex")!=-1) {
               var answer=prompt("What would you like to ask Alex?","")
               var answerlow=answer.toLowerCase()
               if (answerlow.indexOf("read")!=-1 && gotpaper==1) {
                    window.location.replace("address.htm")
               }
               else {
                    alert("Alex looks at me oddly. 'I can read for you if you want,' he says.")
                    }
               }
          else if (answerlow.indexOf("benny")!=-1){
               alert("'Can't right now. Ask Alex,' says Benny")
               }
          else if (answerlow.indexOf("woman")!=-1){
               alert("'Sorry dear, I'm busy right now.  Ask Alex,' she says.")
               }
          else {
               alert("My action has no effect.")
          }
}

}

function seainput(SeaActions) {
     
     if (SeaActions.options[SeaActions.selectedIndex].text == "ask") {
          var answer = prompt("What would you like me to " + SeaActions.options[SeaActions.selectedIndex].text + " Benny?","")
          var answerlow=answer.toLowerCase()
          if (answerlow.indexOf("read") != -1) {
               seeletter1 = 1 
               alert("Benny stares at me for an extended period as if to confirm trust.  His eyes close as if in reflection, only to open again after a deep breath.\n\nHe removes his sweater to reveal a small satchel strung loosely around his neck.  He opens the satchel and removes a stack of what looks like papers tied neatly by a ribbon.  He undoes the ribbon and removes the top paper.  I can see now that the stack is not papers at all but envelopes.  He extends his hand containing the top envelope.")     
          }      
          else {
               alert("Benny ignores my inquiry totally.  'Can you read mister,' he says again.  His expression is staid.")
          }
     }    
     else {
          var answer = prompt("What would you like me to " + SeaActions.options[SeaActions.selectedIndex].text + "?","")
          var answerlow=answer.toLowerCase()
          if (SeaActions.options[SeaActions.selectedIndex].text == "get" && (answerlow.indexOf("envel") != -1 || answerlow.indexOf("paper") != -1) && seeletter1==1) {         
               gotletter1=1               
               alert("I reach for the envelope.  In so doing I brush Benny's hand and am immediately struck by its coldness.  I have not felt such a cold human touch before.\n\nThe envelope has been opened previously.  A smooth tear along the top suggests a letter opener has been used.  I pinch the edges to expose the contents.  Inside is a single sheet of folded paper -- a letter.")
          } 
          else if (SeaActions.options[SeaActions.selectedIndex].text == "read" && (answerlow.indexOf("letter") != -1 || answerlow.indexOf("paper") != -1) && gotletter1==1) {
                window.location.replace("letter1.htm")
          }
          else {
               alert("My action has no effect.")
          }
     }
}

function hqinput(HqActions) {
     var answer = prompt("What would you like me to say?","")
     var answerlow=answer.toLowerCase()
     if (answerlow.indexOf("yes") != -1 || answerlow.indexOf("no") != -1 || answerlow.indexOf("Oui")!=-1) {         
          window.location.replace("letter5.htm")
     }
     else {
          alert("General French stares at me. It is clear that he doesn't comprehend my reply.\n'I was looking for a yes or no,' he says.")
     }
}     

function officeinput(Office) {
     var answer = prompt("What would you like me to say?","")
     var answerlow=answer.toLowerCase()
     if (answerlow.indexOf("yes") != -1 || answerlow.indexOf("no") != -1) {         
          window.location.replace("letter2.htm")
     }
     else {
          alert("The Prime Minister stares at me. It is clear that he doesn't comprehend my reply.\n'I was looking for a yes or no, Sir Charles,' he says.")
     }
}     