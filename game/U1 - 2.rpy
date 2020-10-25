label ep1:
                scene bs
                with dissolve

                default miraclepts = 99
                default parispts = 99
                default sabrinapts = 99
                default sashapts = 99
                default MBpts = 99
                default IApts = 99
                default sabrinaconfide = False
                default miraclekiss = False
                default sasharp = False
                default Iroute = False
                default Broute = False
                default Mroute = False
                default Aroute = False
                default MBlessons = False
                default Ipreg = False
                default DT = False
                default Asex = False

                stop music
                $ player_name = renpy.input("What is your name? Default will be Brandon.")
                if player_name == "":
                    $ player_name="Brandon"
                $ rel_d = renpy.input("What is the girls' relationship to you? Default will be tenant.")
                if rel_d == "":
                    $ rel_d ="tennant"
                $ player_nik = renpy.input("What is the your nickname? Default will be Big Guy.")
                if player_nik == "":
                    $ player_nik ="Big Guy"
                $ rel_f = renpy.input("What is your relationship to the girls? Default will be landlord.")
                if player_name == "":
                    $ rel_f ="landlord"
                soft "[player_nik]."
                "You feel a hand shaking you, but you’re still half-asleep."
                soft "[player_nik]!"
                "The shaking increases."
                P "I’m sleeping."
                soft "You’re supposed to take me to the mall this morning, remember…? My new book got released today."
                scene a1
                with dissolve
                P "That was today?"
                M "Yes… *hesitant nod*"
                play music "GTS - Simple Pleasure Joy.mp3"
                P "Are you sure you just didn’t dream that I promised to take you? You'd be surprised how easy it can be to distort reality."
                scene a2
                with dissolve
                M "P-Please!"
                scene a3
                with dissolve
                P "Alright, alright. I’m getting up. *laugh*"
                P "What time is it anyway?"
                scene a4
                with dissolve
                M "Almost ten. Are you tired? I didn’t hear you come home until really late…"
                P "Yeah. The model at the shoot was a little goblin. No matter how good the photos turned out, she wanted to retake them until they were to her liking."
                P "That’s the last time I do a private shoot for the company."

                M "If you’re that tired, we don’t have to go…"
                "(Miracle's always been the most selfless out of all the girls, so I always give in whenever she wants something for herself.)"
                P "Hey, you trying to cancel our date? It’s too late. You’re not getting away now. *grin*"
                scene a5
                with dissolve

                M "Thank you, [player_nik]…"
                P "I guess I’ll go ahead and get ready, then."

                M "Okay. I’ll make you some breakfast in the meantime."
                P "You’re not gonna give me more of that healthy crap, are you? *frown*"
                scene a6
                with dissolve
                P "I’d rather eat a shoe."
                P "(I’m not exactly a fan of the healthy lifestyle, but I gotta admit eating like that’s probably the reason Miracle is in such good shape, even though she stays cooped up in her room all the time.)"

                M "It’s good for you. I promise you’ll get used to it *giggle*"
                scene a7
                with dissolve
                P "(I’m not a spring chicken anymore, but I think I’m still in decent shape. And I even have the same abs from my college days… kinda.)"
                P "Are you subtly trying to say that I’m old?"
                scene a8
                with dissolve

                M "N-No! I wasn’t saying that at all. Forty is still really young and you don’t even look it. Even my friend Sabrina has a huge crush on you…"
                scene a9
                with dissolve

                M "She made me swear not to say anything! Forget that part, okay?!"
                P "I’ll do my best. *laugh*"
                scene a10
                with dissolve

                M "I just want you to be healthy…"
                scene a11
                with dissolve
                P "I know, sweetie. I’m just messing with you."
                scene a12
                with dissolve

                M "You’re always teasing me. *laugh*"
                scene a13
                with dissolve
                P "That’s 'cause you’re so easy! *yawn*"
                P "Anyway, we should start getting ready…"
                scene a14
                with dissolve
                P "(Oh… I’m sporting some wood.)"
                scene a15
                with dissolve
                menu:
                    "Tell a crude joke":
                        P "Back in the day, they used to call me the Elephant Man."
                        scene a16
                        with dissolve

                        M "Wh-What?"

                        P "Another name was the Wheelchair. Can you guess why?"
                        scene a17
                        with dissolve
                        M "I-I should go make breakfast. B-Bye!"
                        scene a17-1
                        with dissolve
                        P "Because that’s what they needed after a night with me…"

                        scene a17-2
                        with dissolve
                        P "Note to self: joking about your dick being hard in front of a very fragile and emotional girl might have ill effects. *sigh*"
                        P "(I guess I should just get ready for the mall now – if Miracle isn’t too freaked out to go.)"

                        jump promocont1

                    "Try to brush it off [MiraclePath]":
                        $ miraclepts = miraclepts + 1
                        P "It’s just morning wood, honey. Nothing to be shocked over."
                        P "(I’m trying to sound nonchalant, but I couldn't feel any more awkward.)"
                        scene a16
                        with dissolve

                        M "R-Right, uh, sorry… I-I’m gonna go do…. that breakfast thing now, b-bye!"
                        scene a17
                        with dissolve
                        P "…I think that went rather well."

                        scene a17-2
                        with dissolve

                        P "(I guess I should just get ready for the mall now – if Miracle isn’t too freaked out to go.)"
                        jump promocont1

label promocont1:

                scene bs
                with dissolve
                "You quickly get ready."
                scene a18
                with dissolve

                M "Oh, you’re done already, [player_nik]?"

                P "(Good, she’s already recovered – or at least pretending like it.)"
                P "I wish you girls would adopt my habit of quick showers. The water bill this month was almost two hundred bucks."
                scene a20
                with dissolve
                M "You can probably blame that on Paris. She basically lives in the bathroom. *laugh*"
                P "(Ah, yes. My sweet and lovely Paris. She’s the oldest, and couldn’t be any more different from Miracle.)"
                P "(But if Miracle's classified as the 'nerd' and ‘shy’ type, then Paris is the cheerleader who runs the school.)"
                P "(The only problem is that she isn’t a teenager anymore, but still mooching off me like one.)"
                P "So, are you excited to be starting your first year of college after this summer break?"

                M "I guess…"
                P "It could be just me, but you sound the total opposite of excited. *laugh*"
                scene a21
                M "Well, there are going to be so many people that I don’t know and… I don’t know. It just makes me nervous."
                P "(Miracle's been pretty shy since she was young, and I figured she would grow out of it, but she’s eighteen now and doesn’t even leave the house if I or her two sisters aren’t there; her best friend, Sabrina, too.)"
                P "(I really think she might have that phobia of crowds or something.)"
                P "(Maybe I should take her to a shrink? Though I definitely don’t have the cash for some expensive doctor... And it’s my job as her [rel_f] to help her anyway.)"
                P "Maybe you could try staying in the dorms like I suggested before? *hopeful voice*"
                P "(I know I’m pushing my luck after barely convincing her to take classes on campus in the first place.)"
                M "But the college is only twenty minutes away, so isn’t it easier to just stay at home? *quiet voice*"
                P "(I know being close to home is the reason she chose a local school in the first place.)"
                P "But the university would be paying for it, right? It might be a good experience."


                M "I don’t want to talk about it right now… Please?"
                P "Okay. But this conversation isn’t over, alright?"
                scene a22
                with dissolve
                M "Okay…"
                scene a23
                with dissolve
                "Some minutes later, she brings the food to you."
                P "(I know this all looks like the real stuff, but they're just vegan replacements. Ugh.)"
                "As you go to take a bite of the eggs, you pause with the fork at your mouth."
                P "You know, honey… it’s like, kind of hard to eat when you’re staring at me like that."

                M "Oh, sorry. *giggle*"

                M "I used new seasoning, so I just wanted your opinion. But I guess you can tell me after. I’m gonna go get ready!"

                scene a24
                with dissolve
                "You smile as you watch her leave, and finally start on your meal, but quickly regret it."
                P "I was lying before, her healthy cooking doesn’t taste like a shoe. It tastes like a shoe covered in dirt."
                scene a25
                with dissolve
                P "Forgive me, Miracle, but even you aren’t cute enough to make me eat this stuff."

                stop music

                ufv "Caught red-handed!"
                P "I-I didn’t do anything!"
                scene a26
                with dissolve
                play music "GTS - Simple Pleasure Joy.mp3"

                I "You should’ve seen your face. It was so stupid. *snort*"
                P "Isn’t it a bit too early for you to be a jerk? *frown*"


                I "Aww, did I upset the grumpy, old man?"
                P "(She dropped out of college last year, but hasn’t shown any plans of getting a job or going back. I should talk to her later today.)"
                P " I noticed your car wasn’t in the driveway when I came home late last night. Where were you?"

                I "Dinner with my ex."
                P "That’s all?"
                P "(I remember that guy. I never liked him.)"
                scene a27
                with dissolve
                #playsound "I5.mp3"

                I "Why don’t you just ask what you want to ask?"
                P "I wasn’t really…"
                P "(Actually, I WAS kind of alluding to what she’s accusing.)"
                #playsound "I6.mp3"

                I "No. I didn’t fuck him. He wouldn’t stop blowing up my phone, so I only went out with him to make it clear to that I wasn’t interested in fucking lying, dickhead assholes."
                P "Geez, Paris. Could you use more inappropriate language? *sigh*"

                scene a26
                with dissolve

                I "Sure. I actually know some pretty creative names for female genitalia. Wanna hear?"
                scene a28 #mc look down
                with dissolve
                P "I wonder where you got your smartassness from?"
                P "There WERE always questions about your origin…"
                scene a32
                with dissolve

                I "That’s not funny, you’re making it sound like I’m an alien or something. And smartassness isn’t even a word!"

                scene a33
                with dissolve
                P "And while we’re on the subject of things and them being inappropriate, how many times do I have to tell you not to walk around the house half naked?"
                menu:
                    "Steal a peek at those melons [ParisPath]":
                        scene a34
                        with dissolve

                        I "I don’t know why you’re complaining. Seems to me like you don’t mind them much at all."
                        scene a35
                        with dissolve
                        P "Wh-What? I don’t know why you would say that. I’m your [rel_f], Paris."

                        I "And that somehow disqualifies you from being a guy? Unless you decided to go Kaitlyn Jenner without telling us."

                        I "Would you like to make an announcement, [player_nik]?"
                        P "(I’m used to Paris steering things and playing around, but I’m trying to have an important conversation here.)"

                        jump promocont2

                    "Keep your eyes focused on her face like a true gentleman":

                        I "What’s the big deal? It’s not like you haven’t seen me naked before."

                        scene a27
                        with dissolve
                        P "You know, it’s reeeally easy for people to misunderstand when you say things like that. I’m pretty sure seeing you naked when you were younger and seeing you now at twenty-two is a lot different."
                        P "Besides, you barely had mosquito bites back then. *grin*"

                        I "And you call me a jerk?"
                        scene a35
                        with dissolve

                        I "Well, you can’t say that now! So, ha!"
                        jump promocont2

label promocont2:

                scene a37-1
                with dissolve

                tfv "I know you’re always on the lookout for your next sugar daddy and stuff, but could you maybe keep [player_nik] out of your search?"
                play music "Shut Up.mp3"

                scene a37
                with dissolve
                I "Shouldn’t you be sacrificing a virgin in a church somewhere? Or out drinking blood?"

                A "Maybe. But then what would I ever do with my weekends?"

                I "This is why everyone thought you were such a freak back in high school. You don’t even try to deny being so weird."

                A "And why should I give a shit what people think? So I could be popular, and be the school whore – like you?"
                scene a40
                with dissolve

                I "Just because I was popular doesn’t mean I was a whore. But at least I had more than two friends. Loser."

                A "Slut."

                scene a40-1 #cam close
                with dissolve
                P "Ahhh, okay, that’s enough. If you two want to fight, do it somewhere where I can’t see or hear you."
                P "You’re starting to give me a headache and it isn’t noon yet. That’s a record, even for you girls."
                scene a41
                with dissolve

                A "I didn’t want to come out with her here in the first place. But I wanted to ask, are you still coming to my rehearsal today?"
                P "(Shit, I completely forgot, though I probably shouldn’t admit that..."
                P "(How long has it been since Sasha dropped out of college to start acting? About two years? I’ve seen plenty of her plays since… but they’ve all been small performances that have paid next to nothing.)"
                P "(I support her a hundred percent, but I’d be lying if I said I think she's going to make it big anytime soon.)"
                P "Do I ever miss your rehearsals, sweetheart? *smile*"

                A "Yeah. Last week."
                P "*blink*"
                P "Oh. Well, I’ll definitely be there today. I just have to take Miracle to the mall for a new book."
                scene a43
                with dissolve

                I "Why doesn’t she just download them from the internet like normal geeks?"
                P "Can you not call your sister a geek, please? You know she takes that stuff to heart."
                scene a44
                with dissolve

                I "I was jokinggg. *blow tongue*"
                P "Ew. Could you not do that either?"
                scene a45
                with dissolve

                A "I actually think it’s pretty cool Miracle likes real books. Though she could learn to leave the house once in a while."
                scene a40-1
                with dissolve

                I "Why am I not surprised? You think anything weird is cool."

                A "You’re the last person who should be judging -"

                P "Nope! I’m not listening to you two cluck back and forth again."
                scene a48
                with dissolve

                A "What are we, chickens…? *mutter*"
                scene a49
                with dissolve

                A "I was just leaving anyway. You better not be late, [player_name]."

                scene a50
                with dissolve

                play music "GTS - Simple Pleasure Joy.mp3"
                I "Hey, [player_name]."
                P "(I can practically hear the favor she wants to ask already.)"
                P "...Yes?"

                I "Do you mind if I tag along with you and Miracle to the mall? There’s something I want to check out there."
                P "(I want to so call out her little princess act, but I find it hard to say no to her, just like Miracle. Hell, Sasha too.)"
                P "Fine. Just don’t take forever in the shower this time, okay? Because if I’m late to Sasha's rehearsal, she’ll bite my head off."
                P "You know how good Sasha is at giving the cold shoulder when she’s upset."
                scene a51
                with dissolve

                I "I’ll only be an hour."
                P "Paris!"

                I "Hahaha."

                show bs
                with dissolve
                "*minutes later*"
                scene a52
                with dissolve
                P "Sure you don’t wanna sit in the front? Now’s your only chance. *smile*"
                scene a53
                with dissolve

                M "It’s okay. Paris would make me sit in the back anyway…"
                P "Honey, the only way to stop a bully is to give them a good kick in the pants."
                scene a54
                with dissolve

                I "You guys talking crap about me?"

                M "N-No, we weren’t, Paris. [player_nik] was only saying that you’re a bully and I should kick you."
                P "(Another quirk of Miracle is being honest to a fault, and being completely dense in certain situations.)"
                P "(It’s almost impressive, really.)"
                P "Please don’t snitch on your [rel_f]…"
                scene a56
                with dissolve

                I "So, I’m a bully now, am I?"

                P "(I don’t think punching me exactly helps your cause, but it’s always advantageous to play the part of gentleman.)"

                scene a54
                with dissolve
                P "It was a joke. You’re the sweetest [rel_d] a guy like me could ever hope for. *charming smile*"

                I "You’re lucky that I’m such a sucker for flattery. *giggle*"

                "You start the car shortly after and take off to the mall."
                scene a59
                with dissolve
                P "So, what did you want to check out at the mall, Paris?"

                I "Uh, there’s supposed to be panties on sell at one of my favorite shops…"
                P "(I figured it was something like that.)"
                P "Don’t you have enough underwear already?"
                scene a60
                with dissolve

                I "That’s like asking if a monkey has too many bananas. *laugh*"
                P "That was an interesting analogy. I’ll give you points for creativity."
                scene a61
                with dissolve

                I "Hey, Miracle."

                M "Y-Yeah?"

                I "You want me to help you find some new panties?"
                scene a62
                with dissolve
                M "That’s okay, thank you. I just bought some from Wallyworld."

                I "They only sell kids and granny panties there. You’re eighteen now. Aren't you interested in ones more… sexy?"
                P "(Miracle doesn’t care about any of that crap. She practically hides behind my back if a boy looks in her general direction.)"
                scene a63
                with dissolve


                M "A-A little…"
                P "(Or maybe I’m just being naïve. Of course she’s interested in that kind of stuff at eighteen.)"
                P "(Actually, it’s a relief that she is. It’s normal.)"

                I "See, I knew you weren’t as innocent as you pretend to be!"

                scene a61
                with dissolve
                M "I-I’m not pretending…"

                I "Yeah, yeah. I’m sure you would want a pair for your boyfriend or something like that, right?"
                scene a65
                with dissolve

                M "B-B-Boyfriend?"
                P "Oh. I think she’s broken."

                I "I was just poking fun, relax. I know you’re his precious princess anyway, aren’t you? You’re so cute. I bet you would marry [player_nik] if you could."
                P "I think that’s enough joking, Paris."
                scene a60
                with dissolve

                I "Alright, alright. *laugh*"

                M "But that kind of thing wouldn’t be acceptable to other people, right…? *mutter*"

                I "That’s your only problem with it? They’d love you in someplace like Utah, or maybe Alabama."

                scene a67
                with dissolve

                P "(Why is she seriously asking questions regarding us getting married?)"

                scene a68
                with dissolve

                P "Oh..."

                P "(Wait, what the hell am I doing looking between my [rel_d]'s legs? Jesus.)"
                scene a69
                with dissolve
                P "(Oh my god, she caught me looking! How the hell am I going to explain this to her?!)"
                scene a70
                with dissolve
                P "(What…)"

                P "(I’m REALLY happy that I decided to go without sweatpants today, because my dick could cut glass right now.)"
                P "(But that’s not the issue! Why in the world is Miracle showing me her panties?!)"

                I "Uh, [player_nik]?"
                scene a72
                with dissolve
                P "Hello! *bounce in seat*"

                I "Uh, hi. You know you just ran a red light, right?"
                P "*clear throat* W-Well, yeah. I was trying to teach you girls the dangers of driving."

                I "Thanks… but I’d rather not die during your lesson. So, no more running red lights, maybe?"
                P "Uh, you’re probably right. *awkward laugh*"
                show bs
                with dissolve
                "You all reach the city's giant shopping mall and park in the crowded lot."
                scene a73
                with dissolve

                M "Do you remember the name of the book? It’s called Eclipse Awakening."
                P "Isn’t that the name of the book that has those glittery vampires?"
                P "(I never understood the obsession teenage girls had with glittery vampires. Now Dracula, he’s a real vampire.)"
                scene a74
                with dissolve

                M "Y-Yeah. The third book finally came out. I’ve been waiting a whole year for it."

                P "And you’re sure you don’t wanna come in with us?"
                scene a78
                with dissolve

                I "Yeah. If you’re just gonna make [player_nik] pick up the book for you, then what was the point of even coming along in the first place?"

                M "He says that I have to come…"

                scene a79
                with dissolve
                P "Well, it’s the only way you actually leave the house. Your skin needs vitamin D or you’ll start looking like one of those pale vampires!"

                M "*groan*"

                I "*laugh* I think we all know who the real bully is. *laugh*"

                scene a80
                with dissolve
                P "Well, try to sit by the door, so the sun hits you or something."

                scene bs
                with dissolve
                stop music
                "You and Paris enter the mall."
                play music "ITS - Tropical House Dance.mp3"
                scene a81
                with dissolve
                I "Ugh, why are there so many people."
                P "Should Your Highness be the only one permitted to visit the mall whenever thou desires? *British accent*"
                scene a81-1 #I smi;e
                with dissolve
                I "I know you’re joking, but being called 'Your Highness' sounds so natural. What if I’m actually royalty or something?"
                scene a82
                with dissolve
                dou "Hey, you’re totally hot. Why don’t you leave this old dude and come have fun with a real winner?"
                menu:
                    "Just walk away":
                        scene a83
                        with dissolve
                        P "Come on, Paris."
                        dou "Come back here without that loser, baby. I’ll be waiting!"
                        #playsound "I46.mp3"

                        scene a84
                        with dissolve
                        I "That was a lot more anticlimactic than I thought it was going to be."

                        P "(I’m not exactly sure how 'climatic' I was supposed to get there.)"

                        scene a91 #I smi & mc walk
                        with dissolve

                        P "Anyway, where are you taking me?  I still have to go to the bookstore."

                        jump promocont3

                    "Respond to the misdirected youth [ParisPath]":
                        P "Is that usually the way you hit on women?"
                        dou "Yeah, what’s your point?"
                        P "No point, but acting like a Jersey Shore reject might work against you in some cases. And I promise you that my girl is not the type interested in that."
                        scene a85
                        with dissolve
                        dou "What the hell you just say?"
                        P "(I’m far from the confrontational type, but when it comes to my [rel_d]s, I kinda lose my cool.)"
                        scene a86
                        with dissolve

                        I "Sorry. But I’d much rather stay with my BOYFRIEND. And trust me, we have PLENTY of fun all on our own."

                        scene a87
                        with dissolve
                        "Paris licks your cheek sensually."

                        P "(She just loves these types of games, doesn’t she?)"

                        dou "Whatever, i'm out of here. And you’re only sorta hot anyway!"
                        scene a84
                        with dissolve


                        I "*giggle* Did you see that idiot?"

                        P "Boyfriend? Really? Remember that whole thing I mentioned earlier about people and them misunderstanding your words? Well, yeah, this isn’t exactly helping."

                        I "If I remember correctly, which I should considering my spry and youthful age, you called me ‘your girl."
                        P "You know I didn’t mean it like that."

                        I "Oh, stop being so serious! You know how many guys would kill to have a hot piece of ass such as moi hugged up to them?"

                        I "So just shut up and enjoy it while you can."

                        P "*laugh* Fine."

                        scene a91 #I smi & mc walk
                        with dissolve

                        P "But where are you taking me? I still have to go to the bookstore."

                        jump promocont3

label promocont3:

                I "I want a guy’s opinion on the panties I’m going to buy."

                P "Seriously, Paris? I know next to nothing about girl’s underwear and don’t exactly feel comfortable in that kind of place, let alone with you."
                scene a92 #I pout
                with dissolve
                "Paris latches onto you while you walk."
                I "It’ll only be for a sec. I promise. Pleeease, [player_nik]?"
                P "Fine, let’s just get this over with. *sigh*"
                scene a92-1 #i smi
                with dissolve
                I "Yayyy."
                scene a93
                with dissolve
                P "(At least there’s not much people here.)"

                I "What do you think about these?"
                P "Cute, I guess. *shrug*"
                scene a94
                with dissolve

                I "Ugh. I forgot how much of a guy you can be at times."
                P "I’m going to take that as a compliment. *smile*"
                P "(Now that I have her alone, maybe it might be a good time to talk about her future plans.)"
                stop music
                P "Hey, I’ve been meaning to talk about school. Have you made a decision if you’re going back?"
                P "(The last thing I want to do is nag her about it, but it’s been a whole year already, and taking care of three young, adult women isn’t doing any favors on my wwallet.)"
                P "(Especially with the latest news I got last week.)"
                scene a95
                with dissolve
                #playsound "I56.mp3"

                I "I don’t know… I’m just not sure what career path I want to take. If I seriously want to continue my current degree or do something else."
                P "I know it can be tough to figure out what you want to do for the rest of your life, but you can’t just keep going on without doing anything at all."
                scene a96
                with dissolve
                stop music
                play music "I sad - Bleak Moment.mp3"

                I "I know, okay? Do you think I like freeloading off you? *voice tremble*"

                I "You know what, maybe I’ll just move out and find my own place. That way I won’t be a burden to you."
                P "Paris… I never said you were a burden."
                P "(I forgot how emotional she can get at times.)"
                scene a97
                with dissolve

                I "I’m not stupid… I know what you think about me. Sasha certainly doesn’t have any problem saying it, just like she did this morning."

                I "I’m just some whore who'd probably rather screw a senior citizen than work."
                scene a98
                with dissolve
                P "Hey. Don’t ever say anything like that about yourself, okay? You’re a beautiful, young woman who's just trying to find her way in life."
                P "Do you know what I was doing at your age? I could barely wipe my own ass."
                scene a99
                with dissolve
                "She reluctantly laughs."

                I "But you took care of me anyway..."
                P "And I always will, no matter how old you do get. So don’t ever think you’re a burden to me or anything like that, alright? I’ll seriously be hurt if you do."
                scene a100
                with dissolve

                I "Okay… I love you, [player_nik]."
                P "I love you too, sweetheart. And I’ll buy whatever underwear you pick for being a jerk."
                scene a101
                with dissolve

                I "You really don’t have to do that, [player_nik]…"
                P "Isn’t that why you wanted to come along with Miracle and I? *raise* eyebrow*"

                I "Maybe… but after that whole speech, I feel weird about it now."
                P "Sweetheart, it’s fine, really. Just choose what you want, so we can get out of here."
                scene a102
                with dissolve
                play music "ITS - Tropical House Dance.mp3"

                I "You really weren’t lying about not being comfortable here, were you?"


                I "Fine. I’ll just go try on the sets from before. Be right back."
                scene a103
                with dissolve
                P "Hurry up, gal. Time’s a tickin'!"
                scene bs
                with dissolve
                "But not long after Paris leaves, the store’s clerk comes over to inform you, 'your girlfriend needs help back in the dressing rooms.'"
                label galleryScene5:
                scene a106
                with dissolve
                P "(I don’t know why she would need my help trying out underwear.)"
                P "(And I really wish she'd stop calling me her boyfriend.)"
                P "(Though calling me [rel_f] in this situation might be a bit awkward…)"

                P "Paris?"

                I "I’m in this one, boyfriend!"
                scene a107
                with dissolve
                P "*sigh* The lady said you needed help with something?"

                I "Yeah. I just need help deciding between two panty sets. And since you’re the one footing the bill, I figured you should have some say."
                P "I appreciate the gesture, Paris. But I’m sure whatever you decide to get will look fine –"
                scene a108
                with dissolve

                I "Too late!"
                P "*swallow* (Of course Paris is an attractive girl, but she’s my [rel_d] first… Right?)"
                scene a109
                with dissolve

                I "I think I like it. Here’s how it looks from the back!"
                scene a110
                with dissolve

                I "What do you think?"
                menu:
                    "Ask her to turn around again":
                        P "Do you, uh, think you could maybe turn around again? I didn’t get a very good look at the back."
                        scene a109
                        with dissolve

                        I "Oopsie, sorry."
                        scene a110
                        with dissolve

                        I "Do you want to keep staring, or can I change into the other set?"
                        P "Wh-What? I was not staring."
                        P "(Then why did I ask her to turn around when having a good enough view the first time?)"

                        I "*laugh* Sure, hold on."
                        jump promocont4

                    "Compliment her [ParisPath]":
                        $ parispts = parispts + 1
                        P "You… look amazing, sweetheart."

                        I "Thank you!"
                        jump promocont4

label promocont4:
                scene a107
                with dissolve

                I "I can’t get the stupid clasp for the bra on this one. Can you help me out real quick?"
                P "I’ll get the employee…"

                I "*sigh* Seriously? It’ll take two seconds."
                P "(Maybe I am making a big deal out of everything.)"
                scene a112
                with dissolve
                P "Alright."
                scene a113
                with dissolve
                P "There you go."
                scene a114
                with dissolve

                I "Thanks. I think the size is too small on this one…"
                P "(Do not stare. Do not stare.)"
                P "Hm, to be honest, I think I prefer the first set anyway."

                I "Hmm... I think you’re right. Good choice."
                P "Uh, so do you need me for anything else?"
                scene a115 #I laugh
                with dissolve
                I "*laugh* I know you want to leave the girly store. I’ll hurry and get dressed. Thanks, [player_nik]."
                P "(The real reason is because I’m not thinking straight and am afraid I’ll get an erection or something. I need to clear my head.)"
                P "(There’s no way I’m sexually attracted to the girls…)"
                P "(I have to get a grip and just control myself, then everything will go back to normal.)"
                $ renpy.end_replay()
                scene bs
                with dissolve
                stop music
                "After buying Paris' items, you both pick up Miracle's book and leave the mall."
                scene a125
                with dissolve
                play music "GTS - Simple Pleasure Joy.mp3"

                M "I can’t believe it!"

                M "I’m not gonna sleep a wink tonight! Thank you so much, [player_nik]!"

                I "Well, isn’t she precious?"

                P "You’re welcome, baby… But please do try to sleep at least a little. *laugh*"

                "You start driving."

                scene a59
                with dissolve

                I "I’m kinda hungry. Could we stop at Wacdonald's?"
                P "You know they’re super busy in the morning. Just eat when we get home."
                scene a125-1 #i pout
                I "But I like their coffeeee."
                P "Life is full of disappointments, my dear girl. Better you learn that now."
                scene a54
                with dissolve

                I "Yeah? And I bet someone would be really disappointed with certain actions you took this morning."
                P "*heart beat faster*"
                P "You know what, Paris?"

                P "I think we’ll go get that coffee after all."

                I "Oh. Why the sudden change of heart, [player_nik]?"
                P "You’re my darling princess! What else? *loud laugh*"
                scene bs
                with dissolve
                "You soon reach the fast food place and park in the front."
                scene a125-2 #I neutral
                with dissolve
                P "Paris. It’ll be way faster if you go inside."

                I "But that requires walking, and I don’t want to."
                P "I can’t be late for Sasha’s rehearsal, please."
                scene a125-3 #I get out of car
                with dissolve
                I "Argh!"
                scene a131
                with dissolve
                P "(Should I talk about looking up her skirt – and her actually being okay with it?)"
                P "Are you enjoying the book so far?"
                scene a132
                with dissolve
                label galleryScene1:
                M "Y-Yeah… I checked the first few pages already, and it’s even better so far than the second one. Brody confessed his love to Cecelia and then killed his whole evil family who were high vampires."

                M "It’s sooo romantic."
                P "Right… I'll take your word for it. *clear throat*"
                P "Um, I actually wanted to talk to you about something."

                scene a132-1 #M avoid eyes
                with dissolve
                play music "MTS - Relaxed Bossa Nova.mp3"
                M "A-About trying to look up my skirt?"
                P "*wince* (Hearing her ask such an inappropriate question in her cute voice is killing me.)"

                M "It’s okay… I don’t mind if you look."
                P "Miracle, it’s not okay… If people found out, what would they say?"
                P "(Shit, what are you saying! Other people finding out is not the problem; your inappropriate feelings are.)"
                scene a134
                with dissolve

                M "I-I won’t say anything, I promise!"
                P "I know, sweetie... It’s just too risky. Do you understand?"
                scene a135
                with dissolve

                M "I understand… U-Um... Can you close your eyes for a second?"
                P "What? Why…?"

                M "J-Just for a second. *blush*"
                P "(I have a really bad feeling about the next course of events.)"
                scene bs
                with dissolve
                "You feel her put a cloth type material in your hand."

                M "Okay…"
                scene a136
                with dissolve
                P "M-Miracle, what are you doing? *swallow hard*"
                P "(Are these her panties?!)"

                M "Y-You won’t get caught looking now."
                P "That’s not…"

                M "Y-You can smell them if you want…"
                P "Wh-What?"

                M "Guys like that sort of thing, right…?"
                P "Honey, I’m your [rel_f]..."
                P "(I’ve said it a million times, but now I don’t know if I’m saying it for her benefit or mine.)"

                M "I don’t care about that. *confident voice*"
                menu:
                    "Resist your lust":
                        stop music
                        P "I don’t think that’d be a great idea, sweetie..."
                        scene a137
                        with dissolve

                        M "Y-Yeah, you’re right."
                        P "You should put your underwear back on before your sister comes back, okay?"
                        M "Okay… can you please close your eyes again?"
                        P "Oh, uh, sorry. Of course."
                        scene bs
                        with dissolve

                        M "Okay, you can open them now."
                        scene a137
                        with dissolve

                        M "A-Are you mad at me? I'm really sorry."
                        scene a138
                        with dissolve
                        P "Be mad at this adorable face? I think not. *smile*"
                        P "(Of course I’m conflicted with my feelings towards her and vice versa, but the last thing I want to do is screw up our relationship.)"
                        scene a139
                        with dissolve

                        M "Thank you, [player_nik]. *giggle*"

                        M "I love you."
                        P "And I love you more, sweetie pie."
                        jump promocont5

                    "Smell them [MiraclePath]":
                        $ miraclepts = miraclepts + 1
                        P "(Even though I know it’s wrong, my dick can’t stop twitching!) *smell*"
                        scene a140
                        with dissolve

                        M "D-Do they smell good, [player_nik]?"
                        P "(They do smell nice and are soft. And there’s a sticky spot in the middle.)"

                        stop music
                        "You hear Paris burst out from the fast food joint’s front door."
                        jump promocont5

label promocont5:
                $ renpy.end_replay()
                scene a140-1 #m mouth ope
                with dissolve
                P "I can hear your sister coming. Try to act normal, okay?"
                scene a134
                with dissolve
                M "O-Okay!"
                scene a142
                with dissolve

                I "Alright. Let’s rock and roll!"
                play music "GTS - Simple Pleasure Joy.mp3"
                P "I’m glad that’s all it takes to energize you, but try not to get addicted, alright? Too much of that stuff isn’t good for you."
                scene a143
                with dissolve

                I "Mmm… this is so good."
                P "Don’t ignore me…"
                scene a131
                with dissolve
                P "(I’m trying to act normal, but of course I’m still thinking about what just happened with Miracle…)"
                P "(We may have - no, definitely crossed a line today. And I don’t know what to do from here on out, but I have to start controlling myself more.)"
                scene a144
                with dissolve
                stop music
                "Back at the house, Miracle sprints straight for her room, while Paris goes to her own."
                P "(There’s not much time before Sasha's play rehearsal, so we might as well head out now.)"

                P "(I’ve already knocked, but she’s still not answering. Probably blasting music through her headphones like always.)"
                P "Sasha? It’s [player_nik]. Please don’t attack..."
                P "(Last time I entered her room without knocking, she screamed and shoved me out.)"
                scene a145
                with dissolve
                P "(Yup, just as I suspected.)"
                P "(Hmm, I think this is a very appropriate time for a prank. Hehe.)"
                scene a146
                with dissolve
                P "I’ve come to suck your blood! *Dracula voice*"
                scene a147
                with dissolve

                A "Ah!"
                scene a148
                with dissolve

                A "Holy shit! Are you okay, [player_nik]?"
                scene a149
                with dissolve
                P "I just got my ass whooped by my hundred and fifteen-pound [rel_d]. *rub throbbing nose*"
                scene a150
                with dissolve

                A "You’re fine *sigh*"
                P "Where'd you learn to punch like that, anyway?"
                scene a151
                with dissolve
                play music "ATS - Schools Out.mp3"

                A "I’ve been taking boxing lessons at the gym. Pretty good, right? Now bitches can’t fuck with me."
                P "(I know Paris can use some harsh language at times, but Sasha's a natural born sailor.)"
                P "I see… So, are you sure acting is really your true calling? We could turn you into the next Laila Ali."

                A "Yeah? And you'd be my boxing manager? *laugh*"
                P "Yup. I need at least twenty percent."
                scene a152
                with dissolve

                A "What?! No way. Fifteen at most, and that’s only because I kinda, sorta like you."
                P "Fifteen percent and all holidays off, or I walk."
                scene a153
                with dissolve

                A "Hmmm..."
                scene a154
                with dissolve

                A "You drive a hard bargain, Mr. Simpson. But I accept."

                A "So, why were you invading my room?"
                P "I wasn’t ‘invading.’ I knocked and you had your headphones on. Anyway, I figured we'd head to your rehearsal together."
                scene a155
                with dissolve

                A "Oh, shit. I didn’t even know what time it was. Thanks, dude."

                A "Do you want me to drive?"
                P "It’s the least you can do after nearly knocking my head off."
                scene a155-1
                with dissolve

                A "Don’t be a pussy. It was barely a tap."
                P "I’m not a pussy… *frown*"

                scene bs
                with dissolve

                "Taking Sasha's car, you two leave home."

                scene a156
                with dissolve

                "*ring* *ring* *ring*"

                A "Can you check who's calling, [player_nik]?"
                P "As the madam requests."
                scene a157
                with dissolve
                P "It’s an unknown number."
                scene a158
                with dissolve
                stop music
                A "*smack*"
                scene a159
                with dissolve
                P "Uh… ex-boyfriend or something?"

                A "Worse."
                P "(Worse? She must mean HER…)"
                P "Was that… Evelyn –"

                A "Don’t say that bitch's name."
                P "Sasha…. Don’t call your mother a bitch."
                P "(It’s been so long since Evelyn left.)"
                P "(I’d be full of shit if I said her leaving still didn’t bother me, but what kind of [rel_f] would I be to encourage the girls to hate their own mom?)"
                P "(Though all three of them have pretty much expressed they want nothing to do with her. And I can’t say I blame them.)"

                A "To make it worse, she just started reaching out a year ago!"

                A "She has some serious balls, I’ll give her that."
                P "Sasha…"
                scene a160
                with dissolve

                A "You know I hate it when you look at me like that. I’m fine, okay? Anyway, I don’t want to talk about her."
                P "(Sasha’s the toughest out of the girls, for sure. But i know she’s still bothered by being abandoned. Her mother and her were the closest after all.)"
                P "I understand…"
                P "(Probably a good idea to change the subject.)"
                P "So, are you going to be an elf in this play, too?"
                play music "ATS - Schools Out.mp3"
                scene a161
                with dissolve
                A "I-I’m not always an elf."
                P "So, you’re not this time? *smirk*"


                A "S-Shut up."

                scene a161-1
                with dissolve
                scene bs
                with dissolve
                "You two reach your destination several minutes later, which is a dance studio that serves as a rehearsal room."

                scene a162
                with dissolve
                F "Oh, Sasha! I tried calling you a million times!"
                F "Dillon caught a cold, so I canceled rehearsal today."

                A "Ah, it’s not your fault Director Freed. My cell was off…"

                A "Shit. *mutter*"
                F "I’m sorry you two had to make the trip all the way out here."

                A "Dammit. I really wanted to get some practice in today… Actually, since we’re already here, would you mind directing a few of the scenes from the second act of the play?"
                scene a163
                with dissolve
                F "You mean with Letelly and her husband?"
                P "(I don’t like the way I'm being looked at.)"
                scene a164
                with dissolve

                A "You don’t mind playing the husband, right, [player_nik]?"
                P "I don’t know… I’m not really good at this type of thing, Sasha."
                scene a165
                with dissolve

                A "Please, please, pleeease?"
                P "I swear all girls have the natural instinct of 'puppy dog' face… *sigh*"
                P "Fine. What do I do?"
                scene a166
                with dissolve

                A "Thanks, [player_nik]."
                stop music
                "Director Freed goes over the script until you have a good enough grasp of your lines."
                F "Okay. This is the scene where Mookan tells Letelly that he must leave for the war - action!"
                scene a167
                with dissolve
                P "(Okay, this is where I approach Sasha from behind… I think.)"
                scene a168
                with dissolve
                P "(Gotta be careful to keep my crotch from her ass too… or there might be ill effects.)"
                P "Letelly, I know you are upset… but we must take our land back from… And, uh…"
                P "The orcs, if we are to have a future –"
                scene a169
                with dissolve
                F "No, no, no!"
                F "Where is the passion?! The fireworks?!"
                scene a170
                with dissolve

                A "Yeah. That sucked ass."
                P "Well excuse me for sucking ass, but you’re my [rel_d]… It feels weird. *shrug*"
                F "This is not your [rel_d]. This is your wife who you love deeply, and you are being forced to leave, and don’t know if you’ll ever return!"
                scene a171
                with dissolve

                A "Try? Please?"
                "Acting is Sasha’s life, and she’s asking you for help."
                P "I promise I’ll do better. *smile*"
                scene a172
                with dissolve

                A "Thanks, [player_nik]."
                scene a173
                with dissolve
                "Everyone resets their positions and start the scene again."
                P "(I can feel Sasha’s ass against me now, and I'm pretty sure she just tensed up.)"
                play music "All Is Lost.mp3"
                P "Letelly, I know you are upset, but we must take our land back from the orcs if we are to have a future."

                A "I know… I know you must go, but that does not mean I have to be happy about it. *trembling voice*"
                scene a174
                with dissolve

                A "As long as you promise to return to your child, I will not stop you."
                "You try to keep the surprise of Sasha’s superb acting skills from showing on your face, and instead focus on your next line."
                P "You are with child?"
                scene a175
                with dissolve

                A "What do you expect when you ravish me night after night?"
                stop music
                P "(Her talking like that is really making me conscious of how close we are, especially with her tits squished against me.)"
                P "(And her gorgeous face is focused on me too, which is making things so, sooo much worse.) *erection poke her in stomach*"
                scene a176
                with dissolve
                play music "Middle-East-Sneaky-Agent.mp3"
                P "(This is officially the most awkward moment of my life, and probably twice as bad as Miracle seeing my morning wood earlier.)"
                P "(Sasha clearly knows I’m being turned on by her, so there’s no chance of denying that.)"
                P "(Something’s really wrong with me today, with perving out on all three of the girls!)"

                F "That was perfect! If you were a few years younger, Mr. Simpson, I would suggest you for the lead of Mookan. *laugh*"
                scene a178 #A look at crotch
                with dissolve
                F "Okay. Now, go over there for the next scene."

                P "(S-Shit! If I separate from Sasha, he’ll see my hard-on!)"
                F "Is there something wrong?"
                P "Um, well, you see…"
                scene a180
                with dissolve

                A "Actually, Mr. Freed, I’m feeling a bit lightheaded. I think I might have the same bug Dillon got."

                A "Do you mind getting me some water?"
                P "You look fine to me –"
                A "*step on your big toe*"
                F "Oh, of course, sweetheart! Right away!"
                scene a181
                with dissolve
                P "What was that for? *frown*"

                A "For you almost ruining the cover I was giving you?"

                P "(How could I have forgotten about poking my [rel_d] in the gut with my boner only seconds ago?!)"
                P "Sasha, sweetheart, there are no words to explain -"
                scene a166
                with dissolve

                A "*laugh* You’re a guy who was pressed up against a young girl, and your body reacted. Let’s not turn it into a big deal, alright?"
                P "*sigh of relief* (Talk about dodging a bullet. I'm so lucky that Sasha is pretty nonchalant about everything.)"
                P "*smile* Thanks for being so understanding, sweetie."

                A "Sure… but you should learn to control that monster. Think of old, sloppy grandma vaginas or something."
                P "Ugh. That’s disgusting, Sasha…"

                A "That’s the whole point."
                P "*sigh* I actually think it’s working…"
                scene a183 #A reach to touch
                with dissolve
                A "Oh, come here. Let me see."

                scene a183-1 #cam block
                with dissolve

                P "What? No."
                scene bs
                with dissolve
                stop music
                "The director burst into the door only a moment later and forces Sasha to drink."
                scene a185
                with dissolve
                F "I suppose we should call it a day."
                scene a186 #a shout
                with dissolve

                A "No! I’m feeling much better now and I seriously need the practice. Please, Director?"
                scene a185
                with dissolve
                F "I suppose you do look fine... Very well. Shall we do the capture scene next?"
                scene bs
                with dissolve

                "With the happy Sasha, Director Freed explains that the next scene is your character being captured after the war by a human enemy."
                scene a187
                with dissolve
                P "Do I really have to pretend to wear handcuffs?"
                F "It is necessary for the realism of the scene! You must!"

                A "Yeah. Don’t be a spaz."
                P "(I don’t even know what that means, but I’m offended anyway.)"
                P "Hey, I’m helping, aren’t I?"
                P "I guess I’m ready whenever you are."
                F "That's the spirit, Mr. Simpson! Action!"
                scene a188
                with dissolve
                play music "Guardians-Of-Oceanus.mp3"
                A "You knife-ears were actually stupid enough to think you could defeat us?"

                A "I should rip off your cock and make you eat it!"
                P "Wh-What are you doing?!*whisper*"
                scene a189
                with dissolve

                A "Say your line, [player_nik]!"
                P "E-Even if you did that, I would still have a bigger one than you! *grit teeth*"
                F "Yes, Mr. Simpson! I can feel your pain!"
                P "(It’s less pain and more Sasha grabbing my balls in a vice grip. *erection*"
                scene a190
                with dissolve
                play music "Middle-East-Sneaky-Agent.mp3"

                A "Again?! *whisper*"
                scene a185
                with dissolve
                "Sasha makes up another excuse about needing more water to get the director out of the room."
                scene a170
                with dissolve

                A "God! You’re such a horndog, [player_nik]."
                P "Y-You should be happy. It just means I’m healthy? *smile*"
                P "But I think we should probably end it here. Your play is a bit too touchy-feely for me."

                A "Oh my god, I really need to rehearse. The screenwriter from New York is gonna be at the play, and it could be my big break!"
                scene a181
                with dissolve

                A "Look, don’t make what I’m about to say any more awkward than it already will be… But can’t you just jerk off?"
                P "(S-She wants me to masturbate? Out in public?!)"
                P "(First Miracle and Paris, and now things are getting a little inappropriate with Sasha. How does this keep happening?)"
                P "I can… I guess…"

                A "Well, are you waiting for a special invitation? Go whip it out, son."
                P "(My brain is screaming at me to just put a stop to all this… but my dick is saying charge forward.)"
                P "…Alright, I’ll go find a bathroom."

                A "Are you dumb? You run into anyone with that hog of yours, and you’ll be facing more time than Bill Cosby."
                P "Don't call me dumb… But it’s hard to argue with today’s social and political climate."
                P "I’m afraid to look at any woman wrong, for fear she’ll think I’m trying to rape her."
                scene a166
                with dissolve

                A "That’s pretty funny considering you can’t even touch me without getting a woody. And I ain’t talking about Toy Story."
                P "Wh-What? Maybe this isn’t such a good idea after all -"
                scene a181
                with dissolve

                A "Oh my god, I was joking. Look, we’ve stalled long enough. Are you going to do it or not?"
                P "Okay, okay. Don’t rush me. I don’t do well under pressure. It’s the reason I never made the varsity football team."
                P "But where am I supposed to do it?"

                A "Just use the closet room by the studio's entrance door."
                P "Okay… Be right back."

                scene bs
                with dissolve
                stop music

                "You quickly take care of business and return."

                scene a172
                with dissolve


                A "*laugh*"

                P "I-Is something wrong?"
                P "(I can't help but be self-conscious after what I just did.)"

                A "I’m thinking about how ridiculous this whole situation is."

                A "You jerking off to help me rehearse. That doesn’t happen every day."
                P "It’d definitely be an interesting icebreaker at a party. *awkward laugh*"

                A "Ha! Yeah. ‘I saw my [rel_f]'s boners like three times in one day. It was an interesting experience.‘"

                A "So… anyone else have a [rel_f] with a giant dick that could probably destroy Japan?"
                P "Putting aside that you basically referred to my privates as Godzilla, maybe we should keep this a secret between just you and me…"
                A "That sounded sooo wrong *laugh*"

                scene a164
                with dissolve
                A "B-But I promise I won’t tell anyone! I’ll be your good little girl… *innocent voice*"

                P "(I obviously know she’s joking, but she really is a good actor, and her little act's making me horny again...)"

                P "Sasha..."

                scene a172
                with dissolve
                #playsound "A72.mp3"
                A "*laugh* Alright, I’ll stop fucking around now, though. I'm just glad no one noticed anything. If we got caught, we would’ve been so fucked."
                P "(She’s always been a free spirit… not caring about what people think and doing whatever she feels at the spur of the moment.)"

                scene a166
                with dissolve
                A "So, you good now? Or do you need to get another load off?"
                P "I’m good…"
                P "(I still can’t believe I’ve been getting erections because of Sasha just by touching her… What the fuck is wrong with me lately?)"
                A "*sigh* I can already see the guilt and wheels turning in your head."
                A "*laugh* All I did was help out with a problem you were having, nothing more. You’ve done the same for me a million times."
                A "Hell, even right now. I love you, alright, old man? Relax."
                P "*smile* …You really are a smooth-talker. Thanks, Sasha."
                play music "ATS - Schools Out.mp3"

                scene a197
                with dissolve
                A "I know, right? Can I borrow a hundred bucks?"

                P "Ha, you’re not that smooth."

                scene a198
                with dissolve
                "You finish up the rehearsal an hour later. Despite Sasha’s nonchalance about what just happened, you expect the drive back home to be awkward."
                "But she turns the radio's volume up and starts singing, sounding like a cow giving birth."
                "Her usual attitude eases your fears, and lets you know that you have the best girls in the world."
                stop music

                scene bs
                with dissolve

                jump U2
