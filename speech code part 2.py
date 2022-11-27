






def rec():
  return sd.rec(int(duration * rec_rate), samplerate=rec_rate, channels=1, blocking=True)

#creating a dictionary
command_dictionary = {}
command_dictionary['up']= mc.up(0.5, 1)
command_dictionary['forward']=mc.forward(0.5, 0.2)
command_dictionary['back']=mc.back(0.5, 0.2)
command_dictionary['left']=mc.left(0.5,0.2)
command_dictionary['right']=mc.right(0.5,0.2)
command_dictionary['down']=mc.down(0.3,1)

command_dictionary['down']=mc.down
command_dictionary['down'](0.3,1)

def execute_command(command, paramaters):
  command(**paramaters)


for i in range(100):

  audio_command = rec()

  command = classif(audio_command)

  if command not in command_dictionary.keys() | command =='stop':

    break
        #print('Commando non capito bene, ripetere')
        #audio_command = rec()
        #command=classif(audio_command)
        #assert command in command_dictionary.keys(),  f"exit command not expected, got: {command}"
        
    

    
    #if command=='stop':
       #break
       
  execute_command(command_dictionary[command], (1,0))
  print('Give new command')
   
command_dictionary('stop')
print('finish session') 