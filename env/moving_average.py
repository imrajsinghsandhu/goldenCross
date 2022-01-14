# how would i add the last 200 days of prices, and then average them to find the 200 MA?

# create a sum variable, and first initialised to 0
closing_price_sum = 0
MA_days = 200

# now you're opening the data file, and naming it f for this function!
with open('c:/Users/Imraj/Desktop/goldencross/env/data/spy_goldencross.csv') as f:
    content = f.readlines()[-MA_days:] # this will allow you to get the last 200 items of a list 
    for line in content:
        #print(line) # this will allow for line by line printing, vs a whole untidy block of data splashed on terminal  

        # to access the price data from each of the lines, you will first have to split the data at the commas 
        token = line.split(",") # here you choose what element to split the data on
        close = token[4] # 5th item is the closing price that you want!

        # now this assignement statement will increment the above closing_price_sum variable in every loop iteration!
        # however, now TAKE NOTE that the program will read the 'close' variable above as a string value 
        # so you have to cast it to a float value in order for the closing_price_sum to be added in every iteration 
        closing_price_sum += float(close)

# now when the loop is done, you will print out the sum divided by the moving average days u want 
print(closing_price_sum/MA_days)
