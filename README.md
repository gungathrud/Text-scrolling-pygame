load_text_dict() is a function that just makes a dictionary for each letter in the alphabet  it
assigns an image of that letter I made in photoshop as its key, the ' ' and '/' are just placeholders so it doenst crash the program.  
('/' is used for new lines, and ' ' is the spaces)

load_text(text) is the fucntion that loads the text. for every letter you input under 'text' (enter your 'text' as a string
like load_text('hello world'), not load_text(hello world) it adds the image associated with that letter in the dictionary to a list, 'text_list'

draw_text is next in the code but first we need to talk about text_animation(speed), we add the speed input to the counter_txt variable, and this is used to add the letter 
loaded from load_text into the animation list 1 by 1 so it creates the typing effect. If counter = 1, then animation_list = text_list[0:1], then if the speed is 1 the next frame
will be animation_list = text_list[0:2], until all of the text from text_list is added to animation_list

now draw_text(x_pos,y_pos, init) is what you know draws the images in the animation list. if the image is a space (' ') it just adds 5 to the x_pos so the next image
is blitted a little further than normal (you cna get rid of this or change the amount added to the x_pos). if there is a '/', it shifts down and to the right by adding 30
to the y_pos (you can change this to fit however big your letter.png images are) and the init variable is the x_pos you want it to go back to when you are starting
a new line. So if your orignal x_pos you input was 50, and the init you assign is 50, it makes the x_pos start drawing at x=50, the after you draw a word 
it subracts 50 from the x_pos and moves the y_pos down to move down and to the left for a new line

counter_txt_reset just resets the counter variable to 0, this is because if you don't the counter will stay at like counter=30 when the fucntion is doen the first time you run it
so the next time you run it the first 30 letters will e blitted and it'll keep counting from there so you need to reset it to start blitting from 0 again

all_text_func(text, x_pos, y_pos, init,speed) is just a function that calls all the other functions except counter_txt_reset(), this needs ot be called seperately
