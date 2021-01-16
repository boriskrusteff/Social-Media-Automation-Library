# SPL
Automator for Instagram Facebook etc

Requirements:
  1. Install chrome-driver from link
  https://chromedriver.chromium.org/downloads
  
  2. Python 3.8 installed
  
  3. requirements.txt installed
  
  All Methods on Instagram Automator are:
      ->login("email or phone", "password") # require to continue use next methods
      ->find_person("Person ") # require to continue to use send_message
      ->send_message("Message content")
      ->exit_instagram()
      
  
  
  All Methods on Messenger Automator are
      ->login("email or phone", "password") # require to continue use next methods
      ->send_message("username on your friend", "message you wanna send")
      ->exit_fbmessenger()
      
      
  
  All Methods on Facebook Automator are 
    ->login("email or phone", "password") # require to continue use next methods
    ->find_peoples("Person name")
    ->find_posts("Post Title")
    ->find_photos("Photo name")
    ->find_videos("Video name")
    ->find_pagess("Page name")
    ->find_places("Place name")
    ->find_groups("Group name")
    ->exit_facebook()
 
Usage:
  Instagram Automator:
  
    import auto_instagram
    
    instagramer = auto_instagram.Instagram_Automator()
    instagramer.login("your email or phone", "your password")
    instagramer.find_person("person you wanna find")
    instagramer.send_message("message content")
    instagramer.exit_instagram()
      
  
  FB_Messenger Automator:
  
    import auto_fbmessenger

    fbmessengera = auto_fbmessenger.Messenger_Automator()
    fbmessengera.login("Your email or phone", "Your password")
    fbmessengera.send_message("Person you wanna send message", "Message content")
    fbmessengera.exit_fbmessenger()
    
    
  Facebook Automator:
 
    import auto_facebook
    facebooker = auto_facebook.Facebook_Automator()
    facebooker.login("Your email or phone", "Your password")
    facebooker.find_peoples("Person you wanna find")
    time.sleep(10)
    facebooker.exit_facebook()
