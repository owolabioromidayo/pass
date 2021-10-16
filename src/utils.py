def navigate_to_store():
    if self.config.get('PASS_DIR') == None:
        if os.path.exists(self.config.get('PASS_DIR')):
               os.chdir(self.config.get('PASS_DIR'))
    else:
        os.chdir('~/pass')
    
    if not os.path.exists('store'):
       subprocess.call(['touch','store']) 