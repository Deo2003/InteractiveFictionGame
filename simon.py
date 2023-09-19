simon = {
  "story": "AfterDark: Simon's Story",
  "startnode": "1",
  "passages": [
    {
      "name": "Simon's story",
      "tags": "",
      "pid": "1",
      "original": "Having just returned from a grueling 2-hour computer science lab, weariness etched into your features, you honestly aren't too excited about the party. Despite your reluctance, you are determined to honor Mark's (your rooommate) commitment to the party, and drive him and a couple friends to the party.\n\n[[Go to the party->The Party (Simon)]]",
      "links": [
        {
          "original": "[[Go to the party->The Party (Simon)]]",
          "label": "Go to the party",
          "newPassage": "The Party (Simon)",
          "pid": "2",
          "selection": "1"
        }
      ],
      "text": "Having just returned from a grueling 2-hour computer science lab, weariness etched into your features, you honestly aren't too excited about the party. Despite your reluctance, you are determined to honor Mark's (your rooommate) commitment to the party, and drive him and a couple friends to the party."
    },
    {
      "name": "The Party (Simon)",
      "tags": "",
      "pid": "2",
      "original": "At the party, you sticks to the shadows, avoiding the revelry and refraining from drinks. After precisely 30 minutes, you sidle up to an already intoxicated Mark, announcing your departure plan. \"I'm out,\" you murmurs, urging Mark to text you when he's ready for a ride back to the dorm. \n\n[[Head to the car->The Clearing]]",
      "links": [
        {
          "original": "[[Head to the car->The Clearing]]",
          "label": "Head to the car",
          "newPassage": "The Clearing",
          "pid": "3",
          "selection": "1"
        }
      ],
      "text": "At the party, you sticks to the shadows, avoiding the revelry and refraining from drinks. After precisely 30 minutes, you sidle up to an already intoxicated Mark, announcing your departure plan. \"I'm out,\" you murmurs, urging Mark to text you when he's ready for a ride back to the dorm."
    },
    {
      "name": "The Clearing",
      "tags": "",
      "pid": "3",
      "original": "You head back to the clearing in the woods, where you parked your car. Your gaze catches a sight that chills down your spine: a slender, ethereal figure amidst the trees. \n\n[[Get a closer look->Ending1]]\n[[It's probably just a deer->Ending2]]",
      "links": [
        {
          "original": "[[Get a closer look->Ending1]]",
          "label": "Get a closer look",
          "newPassage": "Ending1",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[It's probably just a deer->Ending2]]",
          "label": "It's probably just a deer",
          "newPassage": "Ending2",
          "pid": "5",
          "selection": "2"
        }
      ],
      "text": "You head back to the clearing in the woods, where you parked your car. Your gaze catches a sight that chills down your spine: a slender, ethereal figure amidst the trees."
    },
    {
      "name": "Ending1",
      "tags": "",
      "end": 1,
      "pid": "4",
      "original": "Driven by curiosity, you inch closer to the figure. As you takes tentative steps, A branch snaps behind, and you feel your heart leap into your throat. Whipping back around, you find emptiness where the figure once stood. Heart pounding, you pivot towards your car, but you don't make it any further. Frozen in terror, your screams die with you, strangled by the creature's ghastly assault.\n\n[[You have died->Restart]]",
      "links": [
        {
          "original": "[[You have died->Restart]]",
          "label": "You have died",
          "newPassage": "Restart",
          "pid": "6",
          "selection": "1"
        }
      ],
      "text": "Driven by curiosity, you inch closer to the figure. As you takes tentative steps, A branch snaps behind, and you feel your heart leap into your throat. Whipping back around, you find emptiness where the figure once stood. Heart pounding, you pivot towards your car, but you don't make it any further. Frozen in terror, your screams die with you, strangled by the creature's ghastly assault."
    },
    {
      "name": "Ending2",
      "tags": "",
      "score": 100,
      "end": 1,
      "pid": "5",
      "original": "Dismissive of the figure, you brushes it off as likely being a deer or some innocuous creature. You continue towards your car, get into the driver's seat, and start the engine. You spare one more look up, but find nothing but trees. The drive home is peaceful and you take a nap on the couch, while you wait for Mark's text.\n\n[[You story ends here->Restart]]",
      "links": [
        {
          "original": "[[You story ends here->Restart]]",
          "label": "You story ends here",
          "newPassage": "Restart",
          "pid": "6",
          "selection": "1"
        }
      ],
      "text": "Dismissive of the figure, you brushes it off as likely being a deer or some innocuous creature. You continue towards your car, get into the driver's seat, and start the engine. You spare one more look up, but find nothing but trees. The drive home is peaceful and you take a nap on the couch, while you wait for Mark's text."
    },
    {
      "name": "Restart",
      "tags": "",
      "pid": "6",
      "original": "[[Respawn->Simon's story]]",
      "links": [
        {
          "original": "[[Respawn->Simon's story]]",
          "label": "Respawn",
          "newPassage": "Simon's story",
          "pid": "1",
          "selection": "1"
        }
      ],
      "text": ""
    }
  ]
}