import auto_instagram

instagramer = auto_instagram.Instagram_Automator()
instagramer.login("boris@krusteff.com", "falcon1312")
instagramer.find_person("alex_3618")
instagramer.send_message("My brother everything is fine")
instagramer.exit_instagram()
