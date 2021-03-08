label Iroute:

    "A little time passes and it’s time for you and the girls’ weekly movie night."

    scene j1 #flashback date with Paris
    with dissolve

    "But you can hardly focus with the thoughts of revealing your relationship with Paris, at her request."

    scene bs
    with dissolve

    "And the moment of truth comes as the movie comes to an end."

    scene j2 #All looking at A
    with dissolve

    A "Dude, this might be the best movie I’ve watched in the last five years."

    M "Y-Yeah. I usually stick to romance or anime, but this one was really cool."

    B "I concur. The main character was quite riveting to watch, and he didn’t hold anything back in revenge of his poor puppy."

    A "Right? Especially the last scene where he was fighting like ten dudes."

    scene j3 #A pick up M
    with dissolve

    "Miracle squeals as Sasha easily lifts her."

    A "And it was so badass when he picked up that one and slammed 'em."

    M "*giggle* I-It was, but please don’t slam me."

    I "Guys… [player_nik] and I have to tell you something."

    scene j4 #all look at I
    with dissolve

    B "You have such a solemn look on your face. Is everything okay?"

    M "Yeah, wh-why do you look so serious? Y-You're not sick or anything, are you? Did you go to the doctor?"

    scene j5 #A put down M. Put hand on her head
    with dissolve

    A "Easy, Munchkin. You’re jumping to conclusions again. Let’s just let them say what they have to say."

    scene j6 #A smile at cam
    with dissolve

    A "Besides, I’m sure the news is going to be VERY interesting."

    P "(Ah, I almost forgot Paris already told Sasha what’s up… Did Paris also tell her we were going to announce our relationship today?)"

    scene j7 #B & M smile at I
    with dissolve

    "Sasha sets Miracle down."

    M "S-Sorry for jumping to conclusions like always. I-I'm trying not to do that anymore."

    B "What is the exciting news? I can hardly contain myself!"

    scene j8 #I look away
    with dissolve

    I "Well… there are basically two announcements, so I’m not really sure where to start…"

    P "(It was Paris' idea to tell the girls everything, but obviously she’s nervous.)"

    menu:

        "Let her tell them":

            $ Itell = True

            $ parispts = parispts + 1

            P "(I do want to step in, but maybe it’d be better to let her reveal everything, considering it was her idea.)"

            A "Just start from the beginning. You got this, girl."

            scene j7
            with dissolve

            I "Sash'… Thank you."

            I "Like Sasha said, I guess the best place to start is from the beginning."

            jump U12hug

        "Tell them yourself [ParisPath]":

            $ parispts = parispts + 2

            P "(I’m honestly not sure if Paris would want me to step in right now, but I don’t like seeing her struggle like this.)"

            scene j24 #all neu, look at cam
            with dissolve

            P "I guess it’s better to just start from the beginning. You guys might be surprised at the news, but I promise it’s nothing bad."

            "You speaking up seems to give Paris a bit of confidence."

            scene j25 #I smi
            with dissolve

            I "*whisper* Thanks for stepping in, [player_nik]… I kinda froze up there, didn’t I?"

            P "*smile* Just a smidge. You all good now?"

            I "Mhm. I am."

            scene j7
            with dissolve

            I "Like [player_nik] said, I guess the best place to start is from the beginning."

            jump U12hug

label U12hug:

    I "Obviously Mom leaving affected us all deeply, and I'm no different."

    scene j9 #all neu look at I look down
    with dissolve

    I "I wanted to replace her as the woman of the house… And wrapped up in that was wanting to replace her for [player_nik], too."

    scene j10 #BM surprised
    with dissolve

    "There’s a noticeable silence as you see the wheels in Miracle and Sabrina’s heads start to turn."

    M "W-Wait, So you’re saying that…"

    B "You wanted to be [player_nik]'s woman?"

    scene j11 #I look at group, smi
    with dissolve

    I "Heh. It does sound a bit cuckoo for Cocoa Puffs when you say it out loud like that, but I can’t deny the truth. Yes, I started having those feelings."

    I "They really freaked me out at first, so I tried to ignore them for a long time, but I just couldn’t anymore and revealed my feelings to him…"

    scene j12 #I look at cam.
    with dissolve

    "Paris grabs your hand and squeezes."

    I "And he accepted them."

    scene j13 #all look at cam
    with dissolve

    M "W-Wow. Really?"

    "You start feeling a bit nervous with all the attention switched to you."

    P "*smile* Yeah. I realized she was everything I had been needing in a partner… And we formed a relationship right then and there."

    scene j14 #BM smile. A look at them
    with dissolve

    M "That’s so romantic!"

    B "Indeed! I am quite happy for you two! This truly IS exciting news!"

    A "Nothing surprises the vampire twins for too long, huh?"

    I "*laugh* I kind of have to piggyback what Sasha is saying… You guys really have no problems with [player_nik] and I's relationship? At all?"

    scene j15 #M move
    with dissolve

    M "W-Well, Bina and I have b-been reading those kinds of romance books lately… So maybe that’s why?"

    B "True, we have been quite enamored with them, and we admire the courage of the individuals who challenge the norms of society for love."

    scene j16 #B move
    with dissolve

    A "You sound like a poem."

    B "Hehe. I wasn’t trying, but I really do think these kinds of relationships are something truly special."

    M "B-But didn’t you say you had two things to announce?"

    scene j7
    with dissolve

    B "Oh, you’re right, Miracle. I nearly forgot in all the excitement!"

    I "Well… I’m…"

    scene j12
    with dissolve

    I "No, WE’RE pregnant."

    scene j13
    with dissolve

    M "O-Oh my gosh! Is that true, [player_nik]? You got Paris pregnant?"

    P "Ha. Yes…"

    A "I heard the city’s basketball team needs some shooting help, and obviously you’re a good shot there, Daddy-O. Might want to go tryout."

    scene j7
    with dissolve

    I "*snort* Seriously, Sash'?"

    "You can't help but laugh at the crude joke."
    scene j16
    with dissolve
    B "How far along are you???"

    I "Not long, but we just wanted you guys to know everything."

    M "Th-Thank you for telling us. Sabrina and I will help in any way we can."

    B "Absolutely! We'll be the best aunts in town!"

    scene j17 #BM look at each other. A look at them
    with dissolve

    B "We should gather a few books on pregnancy, just to be a bit more knowledgeable, too."

    M "G-Good idea. I actually think the library downtown has a whole section for that and childcare."

    scene j18 #A smile at cam
    with dissolve

    A "You would think it’s them who’re getting pregnant, eh?"

    P "That goes to show how much they care. And I know you do too, despite your cold and heartless exterior that even make babies cry."

    A "*laugh* You’re such a dick."

    scene j19 #A look at I
    with dissolve

    A "How do you deal with this guy?"

    I "A lot of patience."

    P "*smile* I feel so loved."

    scene j20 #A move, neu
    with dissolve

    A "Hey, but, seriously. Just let me know if you need anything."

    I "You already help me so much listening to all my problems, but I’ll let you know."

    scene j21 #I hug A
    with dissolve

    I "Thank you, Sasha. I love you."

    A "Geez, the hormones are already kicking in."

    scene j22 #MB hug
    with dissolve

    M "Yaaay, group hug!"

    B "Count me in!"

    A "Seriously, guys?"

    scene j23 #cam closer
    with dissolve

    "You join the group hug."

    P "Don’t fight it, Sash'. Just let it happen."

    A "Ugh."

    scene bs
    with dissolve

    "You all continue to talk for a bit longer before everyone heads to bed."

    scene j26 #cam face I
    with dissolve

    P "I gotta say, this feels a lot different."

    I "Us sleeping together?"

    P "Right. Before I’d be paranoid about the door being locked or if anyone could hear us… But all of that’s gone now."

    scene j27 #I move
    with dissolve

    I "You almost sound like you miss it."

    P "I mean, sneaking around like a ninja for sex was a little exciting at first, but the second visit when I stubbed my pinky toe kind of ended that whole fantasy for me."

    I "*giggle* I remember. You sounded like a birthing cow. At least nobody seemed to notice."

    scene j28 #cam touch I face
    with dissolve

    P "So, my beautiful girl. Feeling good about everything?"

    I "Mhm. As you saw, I was super nervous at first, but I should’ve known everyone would be so accepting. It made me want to move all my stuff in here, so it would be official, but I figured it was too late."

    scene j29 #cam touch stomach
    with dissolve

    P "*smile* All we have is time now, and I’ll be here to help every step of the way."

    P "You and the baby."

    I "I know you will."

    scene j30 #I kiss cam
    with dissolve

    "Her soft and moist lips touch yours."

    scene j30-2 #I closeup
    with dissolve

    I "I love you, [player_name]."

    P "(She’s been calling me by my name a lot more recently. I think I prefer it. Makes us feel more like a couple.)"

    P "*smile* I love you more, Paris."

    scene bs
    with dissolve

    "The next months fly by as Paris' belly gets bigger."

    scene j31 #I stand at photoshoot, cam hand on belly
    with dissolve

    P "You doing okay?"

    I "*laugh* For the millionth time, yes. Pregnant women aren’t as fragile as you think. Not this one anyway."

    scene j32 #cam face I
    with dissolve

    P "*smile* Touché, just making sure my girl and baby are alright."

    I "I know. Thank you."

    scene j33 #I kiss cam
    with dissolve

    "Paris kisses you."

    scene j32
    with dissolve

    I "Though to be honest, I might lie even if I wasn’t feeling a hundred percent, because there’s no way I’d miss this photoshoot."

    I "On the cover of an actual magazine? I almost feel like there are cameramen waiting to pop out and tell me it’s all a prank."

    P "*laugh* I know what you mean. Things have been picking up fast, ever since you got that celeb shout-out for your MeTube channel."

    scene j34 #I angry pose
    with dissolve

    I "Hey, what’d I say about that, mister?"

    P "*smile* Ah, my apologies, madam, OUR Metube channel."

    scene j35 #I smile
    with dissolve

    I "That’s more like it. But you’re right. I almost fainted when our video last month got a million views."

    P "And I almost fainted when I saw how much that video made."

    I "Hehe. That too. People have been really enjoying the pregnancy vlogs and fitness videos."

    scene j32
    with dissolve

    I "You might need to knock me up again if our numbers dip after I give birth."

    P "I just love my duties, editing, filming, and making sure you stay pregnant year-round."

    I "*giggle* Remember that. I’m the best partner you’ll ever have."

    P "*smile* That you are."

    scene j36 #cam hold up camera
    with dissolve

    P "So, you ready to look all glam for the pictures?"

    I "Mhm. Just tell me what to do."

    P "(Funny that I’ve wanted to photograph for this magazine practically my whole career. And now the only reason they're letting me is because Paris insisted. But I won’t complain how I got here)."

    scene j35
    with dissolve

    P "Alright, this shoot is to show off all the positive aspects of your pregnancy. So let’s start off easy and just have you hold your belly."

    scene j36-2 #I open mouth hold belly, look at cam
    with dissolve

    I "Hold my belly like this?"

    P "Yep, perfect. Now put on your best smile and look at it."

    scene j37 #I look at belly stiff smile
    with dissolve

    "Paris does as you say."

    P "(Hmm… I’m not feeling any spark from her expression.)"

    scene j36-2
    with dissolve

    I "Is something wrong? You’re not taking any pictures."

    P "It’s my fault. I didn’t properly convey the expression I want you to have. I just told you to do it."

    P "So let’s try this… Look at your belly and just think about the first time you’ll finally get to hold our baby."

    scene j38 #I smile
    with dissolve

    I "Okay. I can do that."

    scene j39 #I big warm smile. Base j37
    with dissolve

    P "There we go, that’s exactly how I want you to look. Keep that pose and expression, Paris."

    scene bs
    with dissolve

    "You take several more shots and eventually finish."

    scene j40 #I looking down at photos
    with dissolve

    I "Oh my… The pictures look amazing!"

    P "It’s easy when you’re working with such a beautiful subject."

    scene j32
    with dissolve

    I "*giggle* I think you’re selling yourself short, Mr. Professional Photographer, but I’m going to accept the compliment anyway."

    scene j41 #cam on I midsection
    with dissolve

    "Your eyes stray down to the twenty-three year-old's body."

    P "(Paris really does look good… I’ve never had a pregnancy fetish or anything, but I’ve been really attracted to her since she got bigger.)"

    menu:

        "[gr]Suggest taking nudes":

            P "(Which gives me an idea…)"

            scene j32
            with dissolve

            P "Think you have enough energy for a couple more pictures?"

            I "Oh, I thought we were done, but sure. This is your world, so I’ll do whatever you need me to do."

            P "Well… What I’m thinking now is taking a few photos for my personal collection."

            scene j42 #I look away
            with dissolve

            I "I know our intimacy hasn't gone down since I’ve gotten pregnant… And much bigger, but I was still worried you were forcing yourself."

            scene j32
            with dissolve

            I "So it makes me feel a lot better that you’re attracted to me even when I do look like a cow."

            P "Paris, you do NOT look like a cow in any shape or form. You look beautiful like I said earlier."

            P "But you know, there are some countries that treat cows as sacred and even worship them, so I would still totally love you if you did become one."

            I "Hahaha. That’s the strangest and sweetest thing anyone’s ever said to me."

            scene j33
            with dissolve

            "Paris can’t hold it in and kisses you for the second time."

            scene j43 #I hug cam
            with dissolve

            I "Thank you, my wonderful man."

            if parispts >= 13:
                label galleryScene16:
                $ iphoto = True
                scene j44 #I look away neu
                with dissolve

                I "And I don’t have a problem taking pics for you, but are you sure no one’s going to walk in on our little photoshoot?"

                scene j43
                with dissolve

                I "The headlines wouldn’t exactly be good. ‘Up and coming Metuber found with her panties around her ankles and [rel_f] with camera in hand.’"

                P "*laugh* I wouldn’t suggest it if I thought we had a chance of being caught. Trust me."

                I "I do."

                P "Good. So what I want you to do is remove your dress, then go back where we took the original photos."

                scene j45 #I take off dress
                with dissolve

                I "I do admit that I like all the comfortable pregnancy clothing. You can pretty much wear a garbage bag and no one will look at you funny."

                P "Ha. I get what you mean. I’d comfortably dress like a bum every day if I could."

                scene j46 #I look at cam
                with dissolve

                I "Or go commando."

                P "That does sound tempting, if not for the part where I feel like my junk would snag on something or a dog would think it’s a toy and decide to take a bite."

                I "*giggle* Oof. You may have a point there."

                scene j47 #I stand naked. Base j32
                with dissolve

                I "Okay, [player_name]. What kind of pose do you want me to do?"

                P "I’m actually going to leave it up to you this time around. You know how to be sexy much more than I do."

                I "Hmm… Okay. I think I have a few poses in mind."

                scene j48 #I hold pussy
                with dissolve

                P "(Mmm, simple, but I like it.)"

                I "Do you like when your girl poses for you? With her big belly?"

                scene j49 #I put hand on belly
                with dissolve

                I "The big belly that has your child growing inside after you came so deep inside me?"

                P "I love it."

                "You didn't expect the dirty talk, but you gladly accept it."

                scene j50 #i backshot
                with dissolve

                I "I know we agreed on keeping the gender a secret, but I think it might be a boy because of all the times you did me doggystyle."

                I "We had sex a lot like always around conception, but I feel like you were doing me from the back a lot more that month."

                P "Can you blame me with an ass like yours? Even Stevie Wonder couldn't resist looking."

                I "Hehehe. You're so silly."

                scene j51 #I on all fours looking back
                with dissolve

                "You follow Paris to the ground."

                I "Tell me, what do you love so much about my ass?"

                P "That’s like asking what a fat kid loves about cake and ice cream."

                I "*giggle* My man is such a charmer…"

                scene j52 #I crouch sexy pose
                with dissolve

                I "It’s no wonder how I ended up pregnant in the first place."

                P "*grin* They did say I had a silver tongue when I was younger."

                I "Mhm... I can certainly attest that hasn't changed."
                $ renpy.end_replay()
                scene bs
                with dissolve

                "You snap a few more pictures and finally finish up."

                scene j32
                with dissolve

                I "I wasn’t expecting the little improvised photoshoot, but it was a lot of fun."

                P "It was. And did I say you’re the best girlfriend in the world?"

                P "(Paris is so open with me, including sexually, so being with her is just too easy.)"

                scene j35
                with dissolve

                I "No, but I humbly accept your accurate praise."

                P "*laugh* I don't know how humble that is, but you do deserve it."

                I "*giggle* Thank you very much. So, are you ready to go home now? I want to finish my pickles and ice cream from last night."

                scene j35
                with dissolve

                P "(I know there are certain women who get unique food cravings, and Paris definitely fits that to a T.)"

                P "Yeah. I actually have to run back out, though. The magazine wants to iron out a few more details for the shoot."

                I "Oh, then I’ll just tag along."

                scene j31
                with dissolve

                P "No, no, no. We’ve already shot a video and did these photoshoots today. You need to take your pretty butt home and rest a little."

                "You gently rub her stomach and she looks at it."

                I "Heh. I guess we have no choice. Daddy says we need to go home."

            else:

                "***You missed a scene because you do NOT have enough points***"

                I  "And I don't mind taking pictures for you, but can we do it at home? I don't exectly feel comfortable getting buck naked out here. What if a bear were to walk in on us?"

                P "*laugh* Right, we wouldn't want that."

                P "(I did want to take some sexy photos out here, but I don't want to push her.}"

                scene j35
                with dissolve

                I "So, are you ready to go home now? I want to finish my pickles and ice cream from last night, too."

                P "(I know there are certain women who get unique food cravings, and Paris definitely fits that to a T.)"

                P "Yeah. I actually have to run back out, though. The magazine wants to iron out a few more details for the shoot."

                I "Oh, then I’ll just tag along."

                scene j31
                with dissolve

                P "No, no, no. We’ve already shot a video and did these photoshoots today. You need to take your pretty butt home and rest a little."

                "You gently rub her stomach."

                I "Heh. I guess we have no choice. Daddy says we need to go home."

                "Paris talks to her stomach."

                jump U12photo

        "Don’t ask":

            jump U12photo

label U12photo:

    scene bs
    with dissolve

    "You take Paris home and soon after go back out like you planned."

    "But not to a meeting with the magazine like you told her."

    scene j53 #B & M excited, A neutral
    with dissolve

    P "Alright, guys. Thanks for meeting me here. And you all didn’t tip Paris off to where you all were going, did you?"

    A "No worries, dude. I told her I was taking the twins out for some ice cream."

    M "I-I don’t like lying to Paris, but this is so romantic and exciting!"

    scene j54 #B close eyes, all look at her dreamy pose
    with dissolve

    B "It truly is. After consummating your love by conceiving a child, you’re going to ask her to be your eternal partner."

    A "Not only do you write books, you even talk it."

    M "*giggle*"

    scene j55 #A look at cam, BM look at A
    with dissolve

    A "And I get you suck at shopping, so you need our help to pick out a ring… But how exactly are you going to pull this off?"

    A "It’s not like you guys can just go out and get married."

    scene j56 #BM sad at cam
    with dissolve

    M "I w-was actually wondering that too, but didn’t want to say anything…"

    B "Yes… I also admit that tidbit was hovering in the back of my mind."

    P "*smile* Don’t worry, guys. The place where I'm taking Paris to propose actually allows us to be married. So after some... special paperwork that I found someone to do, we can be recognized as married in this country too."

    scene j57 #A smile. base j53
    with dissolve

    M "Really?! Yay!"

    B "This is positively brilliant!"

    A "Guess you thought of everything, you criminal. Least you could do after knocking her up."

    P "*laugh* I would’ve done all of this sooner, but I just found out about this loophole and the person who could make it happen. Better late than never, right?"

    P "Now let’s do some ring shopping, girls!"

    scene bs
    with dissolve

    "You and the girls spend some time searching for the perfect ring before you finally decide on one and return home separately."

    scene j58 #I on laptop look at cam, cam at door
    with dissolve

    I "Hey, baby."

    P "*smile* Hi."

    scene j59 #cam closer
    with dissolve

    I "How was the meeting?"

    P "It went well."

    scene j60 #I kiss cam
    with dissolve

    "You kiss her as soon as you reach the bed."

    scene j61 #cam looking at laptop
    with dissolve

    P "What are you up to? Thought you’d be napping by now."

    scene j62 #cam on I
    with dissolve

    I "I was, but I just couldn’t and just started looking at baby names."

    P "Oh yeah? You know I don’t mind anything you choose, as long as it’s not one of those celebrity ones where they try to get all artsy."

    I "What, you don’t think Ocean Sky is a cute name?"

    P "Sounds like a vaginal hygiene product."

    I "*giggle* You’re such a goofball."

    scene j63 #I look at comp
    with dissolve

    I "But I can’t say I disagree with you. I was thinking we could just go simple. Like if it’s a boy, we can just name him after you."

    P "Jr?"

    scene j62
    with dissolve

    I "Mhm."

    P "*smile* I like that. And if it’s a girl?"

    I "Still deciding on that, but maybe something like Olivia."

    P "A pretty name. I wouldn’t have a problem with that. But we still have plenty of time to decide."

    scene j64 #I grab belly look at it, move laptop
    with dissolve

    I "I know we technically do have some time, but it feels like just yesterday I even found out I was carrying your baby inside me."

    I "Still kind of feels surreal."

    P "Nervous?"

    scene j65 #I look at cam, worried
    with dissolve

    I "If I’m being honest? Yeah, I am. What if something goes wrong?"

    scene j66 #cam hand on I belly and her hand
    with dissolve

    P "I promise you everything’s going to go perfect, and I'm going to be right there holding your hand."

    scene j62
    with dissolve

    I "Okay…"

    scene j68 #I kiss cam
    with dissolve

    "…"

    scene j62
    with dissolve

    I "I love you."

    P "I love you too. And I actually had an idea."

    I "Are you rethinking Ocean Sky?"

    P "Haha. Not quite, but you’re in the ballpark. I was thinking we could take a little vacation, just us two."

    scene j69 #I excited pose and exp
    with dissolve

    I "Really? A vacation?"

    P "Yeah. We’ve been working a lot to build the Metube channel all this time that we haven't celebrated its success."

    P "And we might not be able to when the baby comes, so I think we should take the opportunity now. What do you think?"

    I "I think, hell yeah. Just us two on vacation? It doesn't get better than that."

    scene bs
    with dissolve

    "Little does Paris know, you booked the plane tickets in advance and plan to propose to her on the vacation island."

    "And the day quickly arrives where you two fly out."

    scene j71 #I on cam walking in lobby
    with dissolve

    P "How are you doing? I know it was a long flight."

    I "A little tired and aching a bit, but no more than usual."

    P "Well, it’s already kind of late, so we’ll just relax in the hotel room for the rest of the night and go have some fun starting tomorrow."

    I "Sounds good. Just have to rest a little bit and I'll be good to go."

    scene j72 #cam on back of I head, E looking down
    with dissolve

    "You two reach the hotel counter."

    WO "Hello, and welcome to Fakeisland, you…"

    scene j73 #E shocked look at you
    with dissolve

    "The woman trails off as she recognizes you two, and you recognize her."

    P "Evelyn…?"

    EE "[player_name]…"

    scene j74 #E look at I
    with dissolve

    EE "And Paris…"

    I "Mom… What are you doing here?"

    EE "I’m working here… What are you two doing here?"

    P "*clear throat* Here on vacation."

    scene j73
    with dissolve

    "Her question brings you back to your senses as you try to calm your beating heart."

    P "(Is this really happening right now? Evelyn is really here?)"

    scene j75 #E smile
    with dissolve

    EE "I see… For the success of your Metube channel, maybe?"

    I "You know about that?"

    scene j76 #E look at I smile
    with dissolve

    EE "Yeah, I do. I’ve actually been subscribed to you for a little while, and I love your recent videos."

    scene j77 #EE look at I stomach
    with dissolve

    EE "And I have to say, pregnancy really suits you. You are absolutely glowing."

    scene j76
    with dissolve

    EE "I looked like a bear during my pregnancies, so I'm glad you didn't inherit that."

    I "*laugh* Looks like I got lucky."

    EE "Anyway, I know you're probably tired and all that, so I don't want to keep you. But is there any way that we can meet tomorrow for lunch?"

    scene j78 #EE sad face look at cam
    with dissolve

    EE "I… I owe you guys an explanation about me leaving... I’ve been wanting to tell you for a long time now."

    EE "And now that you're here, I don't want to let this opportunity pass by."

    scene j79 #I look at cam mouth open
    with dissolve

    "Paris looks at you for affirmation."

    P "(I’ve tried to forget about Evelyn and her abandonment almost a decade ago now.)"

    P "(But it would be a lie to say that hearing why she left in the first place hasn’t lingered on my mind all this time.)"

    "You give Paris a little nod."

    scene j80 #EE sad look at I and I look at her
    with dissolve

    I "I think it’s fine. Lunch tomorrow, right?"

    scene j76
    with dissolve

    EE "Yes! Thank you so much. And the food here is amazing, so I’ll make sure to have a few things ordered for you guys, on the house."

    I "Thank you. I may not look like a bear as you mentioned, but it wouldn't be an exaggeration to say that I eat like one."

    scene j77
    with dissolve

    EE "*giggle* I totally understand that, but isn't that a total perk of being pregnant?"

    I "Hehe. The top highlight, absolutely."

    "You can't help but smile at the two women getting along."

    P "(Unlike Miracle and Sasha, Paris didn't develop anything negative, per se when her mother left. So I don't think she holds as much of a grudge.)"

    scene j72
    with dissolve

    "They exchange a few more words."

    EE "So, you'll be needing two separate rooms for your stay? Or maybe just one room with two beds?"

    P "(I almost forgot that we need to hide our relationship, so we obviously can't get a single room with one bed.)"

    I "Can we actually get one room with a single bed, please?"

    scene j76
    with dissolve

    EE "The two bed rooms cost the same as the one bed room, so you don't have to worry about that."

    I "I know. We would like the single anyway."

    scene j82 #E confused
    with dissolve

    "Evelyn watches Paris for a second, trying to figure out the request."

    scene j83 #E look at I belly
    with dissolve

    "Her eyes go down to Paris' pregnant belly."

    scene j84 #E look at cam
    with dissolve

    "Then to you."

    EE "I… understand."

    P "(She knows. She absolutely knows. You can say what you want about Evelyn, but she was always damn smart.)"

    scene j76
    with dissolve

    EE "I’ll book that room for you right now."

    I "Thank you."

    scene bs
    with dissolve

    "Evelyn does book the room, and you stand there in a daze until Paris pulls you away."

    scene j85 #I walk in corridor
    with dissolve

    I "I can’t believe we really just saw Mom… All the way out here. Whoever said the world is a small place was not lying."

    P "No kidding..."

    I "I think she knows… everything after my little insistence on the room back there."

    menu:

        "Tell her it’s fine":

            $ parispts = parispts + 1

            P "I do think that’s pretty safe to assume, but it’s fine."

            jump U12truth

        "Dismiss it [ParisPath]":

            $ parispts = parispts + 2

            P "If she knows, she knows. It doesn’t change anything."

            jump U12truth

label U12truth:

    scene j86 #I smile at cam
    with dissolve

    I "Yeah, you’re right."

    scene j85
    with dissolve

    I "And… how do you feel about seeing her? It must’ve been tough for you…"

    P "I’m okay."

    scene j87 #I concerned face cam
    with dissolve

    I "Who am I?"

    P "*raise eyebrow* That a trick question?"

    I "I’m being serious. Who am I to you?"

    P "...My girlfriend?"

    scene j88 #I change put hand on stomach
    with dissolve

    I"And the mother of your future baby. So if you can’t tell me how you’re really feeling, then who can you tell?"

    "You gaze at her pretty, determined face."

    P "(She’s totally right.)"

    scene j89 #cam kiss I
    with dissolve

    "You lean forward for a quick kiss."

    scene j90 #I smi
    with dissolve

    P "Of course you’re right, and I’m acting like a douche in keeping my feelings to myself."

    I "Mhm. Glad you came to your senses."

    P "*smile* Easy when you have a great girl calling you out on your BS."

    scene j91 #cam look away
    with dissolve

    P "But I won’t lie, seeing Evelyn again did bring back old emotions…"

    I "Do… you still have feelings for her?"

    scene j92 #I worried
    with dissolve

    P "Now I have to ask you who do you think I AM?"

    scene j93 #cam grab her belly, use old base render?
    with dissolve

    "You gently hold her big belly."

    P "Evelyn brought NEGATIVE emotions back. You are the only person in this world I am in love with, and I’m crazy about you."

    P "*smile* Like, totally cuckoo."

    scene j94 #I cry
    with dissolve

    I "*sniff* Okay. I love you, [player_name]."

    scene j94-2 #I kiss cyring
    with dissolve

    "You kiss her one more time."

    scene bs
    with dissolve

    "Then you two go to the room for the rest of the night."

    "And when the next day comes, you go to the appointed meeting with Evelyn."

    scene j95 #E smile at cam
    with dissolve

    EE "Thank you guys for coming, seriously… A part of me thought you were totally going to bail. Haha."

    EE "That would have been waaay awkward, but I wouldn’t blame you. It’s what I get for being such a suckish mom."

    "You and Paris awkwardly laugh."

    P "(Looks like Evelyn still has the goofiness.)"

    scene j96 #E surprised look at cam
    with dissolve

    EE "Oh my god… I’m being totally weird right now, aren’t I?"

    I "N-No, not totally…"

    EE "I totally am!"

    scene j97 #E deep breath
    with dissolve

    EE "Calm down, Ev'. You got this. Just act normal like you practiced in the mirror last night."

    scene j95
    with dissolve

    EE "Uhhh… Do you guys think we could maybe start over and pretend that never happened?"

    I "*laugh* Sure… Why don’t you just start with what you have to tell us?"

    "You smile and nod in agreement."

    scene j98 #E smi at I
    with dissolve

    EE "I think that’s probably a good idea… I’d like to explain to you everything regarding my absence in your life."

    I "Whenever you’re ready. Take your time."

    EE "Thank you, Paris…"

    "Once again, you’re impressed by Paris' maturity."

    scene j99 #E look down
    with dissolve

    EE "I guess I should start by saying that I wanted you to hate me, but you’re being so nice… Which almost makes me feel worse."

    scene j100 #I confused
    with dissolve

    I "I’m not sure I quite get what you’re saying. You WANTED me to hate you?"

    "You’re just as confused, but stop yourself from asking a million questions as Evelyn prepares to speak again."

    scene j100-2 #I neu, E look at I
    with dissolve

    EE "Heh, yeah. My plan kinda backfired, though."

    scene j100-3 #I neu E deep breath
    with dissolve

    EE "*deep breath* You got this, girl. Just explain everything to them like the doc said."

    scene j101 #E neu look at I
    with dissolve

    EE "The reason why I left isn’t a complicated one, but it’s very deep."

    scene j102 #E look down
    with dissolve

    EE "Growing up, my parents hurt me. A LOT. In ways that no child deserves. My father was the main culprit, but my mother pretended like nothing was going on."

    EE "So she can go to hell for all I care."

    scene j100-2
    with dissolve

    EE "*laugh* I’m sorry. I really shouldn’t say that."

    scene j100-3
    with dissolve

    EE "*deep breath* Just relax. You’re fine."

    P "(So… that’s why she never wanted me to meet her parents? I thought it was because they lived in a faraway country…)"

    scene j101
    with dissolve

    EE "I won’t go into detail about the abuse, but it was long and it affected me in every single thing that I did, despite my best efforts to just bury it all."

    scene j102
    with dissolve

    EE "But I couldn’t."

    EE "I tried to kill myself, on more than one occasion."

    scene j103 #I surprised
    with dissolve

    P "What?"

    I "You tried to commit suicide…?"

    EE "Yeah. I did."

    "Your mind reels back to around the time she left."

    scene j104 #E smi at cam
    with dissolve

    P "So… that one night when you cut yourself on accident…"

    EE "Yep."

    P "And the time you had to get your stomach pumped because you accidentally took too many pills…"

    scene j105 #E raise two fingers
    with dissolve

    EE "Attempt number two right there."

    P "*whisper* Jesus…"

    P "(How the fuck did I not know she was dealing with childhood abuse all that time???)"

    scene j104
    with dissolve

    EE "I know what you’re probably thinking right now. That it’s your fault or you could have done something different, but none of that is true."

    EE "I was SERIOUSLY screwed up, man. And instead of burdening you guys with all that and having you worry, I left."

    EE "That way you guys could just live your lives."

    P "So that’s why you…"

    scene j98
    with dissolve

    I "And how are you doing now? You look happy and healthy."

    EE "That I am Paris, and I am so happy you said that, thank you. It took a shit ton of therapy and mental hospital stays, but I’m honestly better now."

    EE "Not perfect, but hey, who isn’t a little crazy?"

    scene j106 #I move hand or something
    with dissolve

    I "*giggle* That’s like my life motto since I became pregnant and scatterbrained, so I totally feel you on that."

    I "And now that you’ve explained your side of leaving, it makes a lot more sense. Can I go ahead and respond to it?"

    EE "Absolutely. I want you to be honest with me even if you're afraid of hurting my feelings."

    I "I will because I do think it is important to get everything out on the table right now, and have no regrets."

    scene j107 #I neu look to the side
    with dissolve

    I "There’s a lot I would like to say…"

    "Paris takes a moment to think."

    P "(Paris seems to struggle with these big conversations, not that I blame her. A lot has been happening recently.)"

    scene j100-2
    with dissolve

    I "Can I assume you know who the father of my child is?"

    EE "Yes…"

    scene j108 #E look at cam
    with dissolve

    EE "I think so."

    P "(Well, that confirms it. But I can’t read her right now. Is she pissed about it? Hurt?)"

    scene j100-2
    with dissolve

    I "I understand that just finding it out was a total shock… And even more so after hearing about your own situation…"

    I "But I can promise you it’s not like that, even a little bit with [player_name]. He makes me feel special every day and treats me like a queen."

    I "Not saying he’s perfect, by any means. He leaves his clothes on the floor and forgets to leave our bathroom seat down, despite me reminding him a million times…"

    scene j109 #I smile at cam. E smi look at cam
    with dissolve

    I "But I love him more than anything and I couldn’t imagine being with another man."

    P "Shaky in the middle there, but good landing."

    I "*giggle*"

    scene j110 #I surprised at E who smile at cam
    with dissolve

    EE "I believe you."

    I "You do? Just like that?"

    scene j111 #E smile at I
    with dissolve

    EE "I do. Like I said yesterday, I’ve been subscribed to your channel for a while now, so I’ve seen how you guys interact."

    EE "How you look at him and light up like a kid opening their first present during Christmas. That’s the look of someone in love."

    scene j112 #I embarrassed smi touch hair look away
    with dissolve

    I "Man, do I really act like that on camera? Kind of embarrassing."

    EE "There’s nothing to be embarrassed about when you’re in love."

    scene j98
    with dissolve

    I "Heh, you’re right."

    EE "Can I ask how your relationship started in the first place?"

    I "That question actually ties in with your leaving, so I’m glad you asked."

    scene j100-2
    with dissolve

    I "I don’t want you to feel like I'm blaming you or anything, but I do want you to understand. Okay?"

    EE "Of course, honey. I’m all ears."

    I "Good. So, when you did leave, I was mad and confused for a little while, but I was more concerned with how Sasha and Miracle were effected."

    I "They were younger, so of course they took it harder. Seeing that, I swore to myself to fill in the role you left empty and become the woman of the house."

    scene j113 #E shift pose, sad
    with dissolve

    EE "So my leaving did affect them, too…"

    I "Unfortunately, yes. But I would rather you talk to them and find out everything from their perspective."

    EE "I understand and I agree. I should be hearing what they went through, and still are from them."

    scene j100-2
    with dissolve

    I "Like I was saying, I wanted to fill your shoes for the girls… And for [player_nik], which manifested into romantic feelings."

    I "I hid them for a long time until I couldn’t anymore and finally confessed my feelings for him last year."

    scene j114 #I smile, E surprise
    with dissolve

    EE "God, I can only imagine how nervous you felt!"

    I "No kidding. I literally ran away from him right before I confessed and he had to track me down."

    EE "Looks like running away is in our DNA, eh?"

    I "Hahaha. I guess it is."

    scene j109
    with dissolve

    I "But I’m lucky he did come and find me, otherwise we might not be together today."

    EE "Of course some would frown on your relationship, but I can honestly say [player_name] is the best man I have ever known."

    EE "And you have become such an amazing young lady, and you two really do seem to love each other. And that's all that matters in my book."

    scene j98
    with dissolve

    I "Thank you… Mom. That means a lot. And now that I do know your circumstances, I would like to start establishing a relationship with you."

    scene j115 #E excited pose
    with dissolve

    EE "Are you kidding me? That would be freaking amazing."

    I "*laugh* I think so too… As long as you don't have any ideas of taking my man back?"

    EE "Hahah. I've done enough damage, so not even a thought in my head. And I very much doubt I could if I even tried."

    scene j115-2 #E & I look at cam
    with dissolve

    EE "It's obvious the guy is like crazy in love with you."

    P "I became her partner to have a reason to stalk her all day. That's how deep my love for her is."

    I "Hehehe."

    scene bs
    with dissolve

    "The days fly by as you and Paris enjoy your vacation until the end nears, and you take her out on your final night."

    scene j116 #I look at waiter who face hidden
    with dissolve

    I "Yes, I'm ready to order. Can I have the sea bass with broccoli and rice on the side. The macaroni and bread sticks, and also mashed potatoes."

    I "And can I also have the..."

    "Paris rips off a few more orders before the waiter nods and leaves."

    scene j117
    with dissolve

    P "Is it weird that I wish I was pregnant, just to be able to eat like that?"

    I "*giggle* What, the swollen ankles and muscle aches all over don’t make it attractive enough?"

    P "On second thought… Nevermind. *laugh*"

    P "But you’re a warrior. We’ve enjoyed pretty much everything this island has to offer without slowing down much."

    scene j118
    with dissolve

    I "Maybe because I’m still pretty young and it’s my first pregnancy? I’m sure I’ll be complaining and refusing to go out by my third one."

    P "(We never talked about how many kids we’ll have, but Paris certainly seems to want more than one… And I think I’m good with that.)"

    P "No problem. We’ll use the kids as Santa does his reindeer and have them carry you everywhere."

    scene j117
    with dissolve

    I "Hehehe. I don’t think we’ll be winning any parent of the year awards if we do that… But I’m with you, papa."

    scene bs
    with dissolve

    "You and Paris enjoy your meal while you continue to talk."

    scene j119 #I with a lot of food on table. Base j117
    with dissolve

    P "(Okay, the band I hired should start playing soon… And then it’ll be time to propose.)"

    "You realize you’re probably the most nervous you’ve ever been."

    P "*deep breath* (Just relax and do everything like you planned )"

    scene j120 #I look at cam
    with dissolve

    I "[player_name]. You okay?"

    P "Y-Yeah, of course. I’m good."

    scene j121 #I confused look to band
    with dissolve

    "And right on time is the band that immediately starts playing."

    scene j122 #I excited at cam
    with dissolve

    I "Haha. Is that my favorite song???"

    "You smile and nod at her."

    "'I love you' she mouths."

    scene j123 #I excited at band
    with dissolve

    "Paris resumes listening to the band."

    scene j124 #MC play guitar. I excited 3rd
    with dissolve

    "You wait until the chorus to grab a guitar from one of the guys like rehearsed and start playing."

    I "Oh my god!"

    "Paris can’t stop laughing with an excited expression as you start singing."

    "The song goes on for a couple of minutes while you do your best not to screw it up and finally do finish."

    scene j126 #I excited. 1st
    with dissolve

    I "Babe, that was so amazing!"

    scene j127 #I kiss cam
    with dissolve

    "…"

    scene j127-2 #I sit normal
    with dissolve

    I "Since when the heck did you start playing guitar and singing?"

    P "*laugh* Like last month?"

    P "(The lessons weren’t cheap, neither was hiring this band and renting this place out for the hour, but it's all worth it just to see such a happy look on my girl's face.)"

    scene j128 #look to side
    with dissolve

    I "No wonder the restaurant is empty."

    scene j127-2
    with dissolve

    I "Seriously, baby. This might be the sweetest thing anyone’s ever done for me, and you’ve already done plenty."

    I "You are sooo getting some tonight."

    "The men behind you make awkward noises and look away."

    P "(Now it’s THAT time.)"

menu:

    "Don’t propose":

        scene j129 #cam look down at self, on one knee
        with dissolve

        "Your body won’t move as you command it to take out the ring."

        P "(Maybe… maybe I’m just not ready to take our relationship to that level yet. Obviously Paris is pregnant, but is adding marriage really the right thing to do?)"

        "You rack your brain for a solution."

        I "*laugh* Baby? You gonna stay down there forever?"

        scene j127-2
        with dissolve

        P "Ha, no. Performing is just a lot more tiring than I thought it would be. Just give me a sec."

        P "(Yeah… I don’t think right now is the best time after all. Not saying forever, just right now.)"

        scene bs
        with dissolve

        "The band already clued in on the plans to propose look confused when you thank and dismiss them, but they leave without saying anything."

        "And you and Paris spend the rest of the night together before going home the next day."

        jump U12ring

    "[gr]Propose":

        if parispts >= 15:

            scene j129
            with dissolve

            "You hesitate for a bit as you reach for the ring."

            P "(Of course I’m nervous. I'm about to propose to the one of my dreams. But even if she did reject me, I wouldn’t regret this moment.)"

            I "*laugh* Baby, you gonna stay down there forever?"

            P "Nope, just until you say yes."

            I "Say yes? To what?"

            scene j130 #I shocked look at ring proposing. 3rd
            with dissolve

            I "What… that…"

            P "Paris Carolyn Simpson, will you marry me?"

            scene j131 #I cover mouth crying look at ring. 1st
            with dissolve

            "Paris starts crying at once as her entire body trembles and shakes."

            "The seconds tick by as she just stares at the offered ring, making you even more nervous."

            P "P-Paris?"

            scene j132 #I hold out one hand
            with dissolve

            "Calling her name seems to bring her back to the current situation, and she offers you her trembling hand."

            P "*laugh* I’m going to take that as a yes."

            scene j133 #put ring on finger
            with dissolve

            "You put the ring on Paris' finger, which isn’t so easy because of her shaking, but you manage after a few tries."

            scene j134 #I excited look at ring
            with dissolve

            "She stares at it for a bit, almost like it’s a winning lottery ticket."

            scene j135 #I grab cam face kiss
            with dissolve

            "Then she pulls you into a passionate and deep kiss, sticking her tongue into your mouth."

            P "(Ha. Something tells me she approves of the proposal.)"
            label galleryScene17:
            scene j136 #move to hotel
            with dissolve

            "The kissing doesn’t stop when you move to your hotel room as she hurriedly removes your clothes."

            scene j137 #I break kiss to remove own clothes, break kiss
            with dissolve

            "She breaks the kiss to take off her own clothes, finally letting you get some air."

            scene j138 #I grab face again to kids. Base b136
            with dissolve

            "But she’s back on you again as soon as her dress hits the floor."

            "You spend a little more time exploring each other’s mouths before she pulls you to the bed."

            scene j139 #Side fuck 3rd
            with dissolve

            "And pushes her ass back into your dick, so you have no choice but to penetrate her, not that you mind."

            "Once again, you let out a pleasurable moan at feeling the sensation of Paris' pregnant pussy."

            "It’s more wet and sticky, and her walls feel a lot softer as they hug and massage your dick at the same time."

            scene j140 #Front angle
            with dissolve

            "With her pussy being mushy and soft, it’s not as tight, so you’re easily able to reach the very end, and you stay there for a second."

            "Enjoying the new incredible feel of her insides. Paris never stops kissing you while you pull out, separating her tunnel, then plunging deep to hit bottom again."

            scene j141 #closeup
            with dissolve

            "Even though your strokes are strong and steady, you make sure to go slow, obviously because of your child growing inside her."

            P "(The positions for sex have definitely been limited since she got pregnant, but it hasn’t been a problem at all.)"

            "You pump into her for a little bit, feeling her get even wetter, so each collision into her pussy makes a loud 'squelch,' like you’re mixing a pot of very cheesy macaroni."

            scene j142 #I leg up, rub clit
            with dissolve

            "You know that means she’s getting near completion and that’s confirmed when she raises her leg to allow you even easier access."

            "So you start fucking her a little faster, burying your cock into her pregnant pussy over and over again, and it happily swallows you each time."

            "Paris' kissing also gets more aggressive as she seems to try to cover your entire mouth with hers while wrapping her tongue around yours even harder."

            scene j143 #back shot
            with dissolve

            "She furiously rubs her clit the whole time, getting closer and closer to orgasm, until she finally does."

            I "Oh my god…!"

            "Her whole body tenses up like you told her to 'freeze' and she just vibrates as a wave of hot pleasure passes from head to toe."

            scene j141
            with dissolve

            "You’re not done yet, so you lower her leg back down and slide in and out of her."

            "Her pussy is still in the throes of an orgasm, so it’s clamped down on you hard, squeezing and pulsating on your own throbbing dick."

            "So you’re able to reach your climax in no time and blast your load as deep as you can."

            scene j144 #creampie
            with dissolve

            "Your hard breathing joins Paris' as you pull out, letting your cum escape and dribble out of her."

            scene bs
            with dissolve

            "You two catch your breath for a bit before cleaning up and cuddling."

            scene j145 #I face close
            with dissolve

            I "If I wasn’t pregnant already, I’m very sure I would be right now. I think you came a bit more than usual."

            P "Can you blame me? You basically dragged me in here and had your way with me."

            I "*giggle* I guess I did, didn’t I? It’s just that I was filled with so much emotion after you proposed."

            scene j146 #I look at ring
            with dissolve

            I "I still kind of am, to be honest."

            P "*smile* I’m just glad you accepted. I was on the verge of needing new pants when you didn’t answer at first."

            scene j145
            with dissolve

            I "Hahah. Glad we were able to avoid that, but you should’ve known you had nothing to be afraid of. You’re the man of my dreams."

            P "And you’re the woman of mine."

            I "Hehe."

            scene j147 #I neu look down
            with dissolve

            I "But how would we even get married…? It’s impossible…"

            P "Not as impossible as you think."

            scene j148 #I surprised at cam
            with dissolve

            I "What?"

            P "*smile* I found a loophole that lets us get married here, so that we can make it official back home with a little finessing here and there."

            scene j149 #I excited
            with dissolve

            I "Oh my gosh, babe, that’s amazing! Give me a kiss!"

            P "(Hard for her to get up in this position.)"

            scene j150 #I kiss cam
            with dissolve

            "You give a quick kiss."

            scene j146
            with dissolve

            I "I should have known you would have a plan."

            P "I forgive you, but no doubting me again."

            I "*giggle* Yes, sir. So how exactly do we do everything?"

            P "Well, I figure you can plan the wedding and all that good stuff, then we get married over here. And it’s pretty private here, too. Everyone minds their business."

            scene j147
            with dissolve

            I "Hmm…"

            P "What are you thinking about?"

            I "Nothing… just that I do know a lot of celebrities come over here to get away from all the cameras and craziness…"

            "You try to understand what Paris' thought process is."

            P "Is… moving over here something you would want to do?"

            scene j148
            with dissolve

            I "That’s not something we could really do, is it? What about the girls?"

            "You can obviously hear the hope in her voice."

            P "Sasha got the role in Sarah Green’s play, so she's moving to New York pretty soon. And Miracle’s doing way better in school. Even has other friends besides Sabrina, which will be there for her anyway, along with Sabrina's mom."

            P "I’m not saying we move here tomorrow, but in the next year or two while we plan the wedding, we can start moving things along."

            scene j149
            with dissolve

            P "And… start our family out here. I have a feeling we’ll be needing to expand after this baby anyway. What do you think?"

            I "Hehehe. I think you’re an absolute genius!"

            scene j150
            with dissolve

            "…"

            scene j149
            with dissolve

            I "I can’t wait to officially start our lives together out here as husband and wife."
            $ renpy.end_replay()
        else:

            "***You do NOT have enough points for this choice***"

            scene j129 #cam look down at self, on one knee
            with dissolve

            "Your body won’t move as you command it to take out the ring."

            P "(Maybe… maybe I’m just not ready to take our relationship to that level yet. Obviously Paris is pregnant, but is adding marriage really the right thing to do?)"

            "You rack your brain for a solution."

            I "*laugh* Baby? You gonna stay down there forever?"

            scene j127-2
            with dissolve

            P "Ha, no. Performing is just a lot more tiring than I thought it would be. Just give me a sec."

            P "(Yeah… I don’t think right now is the best time after all. Not saying forever, just right now.)"

            scene bs
            with dissolve

            "The band already clued in on the plans to propose look confused when you thank and dismiss them, but they leave without saying anything."

            "And you and Paris spend the rest of the night together before going home the next day."

            jump U12ring

        jump U12ring

label U12ring:

scene bs
with dissolve

"THIS CONCLUDES PARIS' ROUTE!"

"THANK YOU FOR PLAYING, AND IF YOU WOULD LIKE TO SEE A PICTURE PERFECT SEQUEL, THEN PLEASE THINK ABOUT BECOMING A PATRON TO SHOW YOUR SUPPORT AND LET ME KNOW!"

jump mm
