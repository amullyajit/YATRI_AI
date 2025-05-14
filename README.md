# YATRI_AI
ALGORITHM :-
BEGIN YATRI_AI
    INITIALIZE text-to-speech engine
    INITIALIZE speech recognition engine
    LOAD traffic prediction AI model

  FUNCTION speak(text):
        CONVERT text to speech
        PRINT text to console

  FUNCTION listen():
        LISTEN for user voice input
        CONVERT speech to text
        RETURN recognized text (or error message if failed)

  FUNCTION predict_traffic():
        IF AI model is loaded:
            ASK user for hour of the day
            GET user input
            
  ASK user for day of the week
            GET user input

  ASK user for vehicle counts (cars, bikes, buses, trucks)
            GET user input

  COMPUTE total vehicle count
            PREDICT traffic congestion using AI model
            CONVERT prediction into "low", "normal", or "high"
            SPEAK the predicted traffic condition
        ELSE:
            SPEAK "Traffic model is not available."

   FUNCTION chatbot_response(user_input):
        MATCH user input with predefined chatbot responses
        RETURN the best-matched response (or default response)

  FUNCTION yatri_ai():
        SPEAK "Hello! I am YATRI AI. How can I assist you?"
        
  WHILE True:
            GET user voice command using listen()
            
  IF command contains "traffic":
                CALL predict_traffic()
            
  ELSE IF command contains "exit" OR "stop" OR "bye":
                SPEAK "Goodbye! Drive safely."
                BREAK loop
            
  ELSE:
                GENERATE chatbot response using chatbot_response(command)
                SPEAK the response

CALL yatri_ai() TO START THE SYSTEM

END YATRI_AI
