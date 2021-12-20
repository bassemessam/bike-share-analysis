import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_dict={'january':1, 'february':2, 'march':3,'april':4,'may':5,'june':6, 'all':7}
weekday_dict={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,
'saturday':5,'sunday':6,'all':7}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see the data for Chicago,New york city, Washington? ").lower()
            while city not in CITY_DATA.keys():
                city = input("Please enter a valid city name from these options (Chicago,New york city, Washington) ").lower()

            month = input("Would you like to filter the data by month,or not at all? (january, febrauary, march, april, may, june, type \'all\' for no month filter) ").lower()
            while month not in month_dict.keys():
                month = input("Please enter a valid month name from these options (january, febrauary, march, april, may, june, type \'all\' for no month filter)) ").lower()

            day = input("Which day are you interested in? (saturday, sunday, monday, tuesday, wednesday, thursday, friday,type \'all\' for no day filter ").lower()
            while day not in weekday_dict.keys():
                day = input("Please enter a valid week day from these options (saturday, sunday, monday, tuesday, wednesday, thursday, friday,type \'all\' for no day filter ").lower()

            print("Thank you for your input, Here is the analysis...")
            break
        except KeyError:
            print('Your inputs are invalid')



    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour
    df['Trip Duration'] = (df['End Time'] - df['Start Time']).astype('timedelta64[m]')
    if month == 'all' and day == 'all':
        filtered_df = df

    elif month != 'all' and day == 'all':
        filtered_df = df[df['Month']==month_dict[month]]

    elif month == 'all' and day != 'all':
        filtered_df = df[df['Week Day']==weekday_dict[day]]

    elif month != 'all' and day != 'all':
        filter_month_df = df[df['Month']==month_dict[month]]
        filtered_df = filter_month_df[filter_month_df['Week Day']==weekday_dict[day]]


    return filtered_df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    month_list=['January', 'February', 'March','April','May','June']
    weekday_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    # TO DO: display the most common month

    result_month = month_list[df['Month'].mode()[0]-1]
    print("The most common month is {}".format(result_month))

    # TO DO: display the most common day of week
    result_day = weekday_list[df['Week Day'].mode()[0]]
    print("The most common day of week is {}".format(result_day))

    # TO DO: display the most common start hour
    result_hour = df['Hour'].mode()[0]
    print("The most common hour is {}".format(result_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_end Stations'] = df['Start Station'] + " <> " + df['End Station']
    start_end_comb = df['Start_end Stations'].value_counts().sort_values(ascending=False).index[0]

    print("The most frequent combination of start and end stations are {}.".format(start_end_comb))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {} minutes.".format(round(df['Trip Duration'].sum(),2)))

    # TO DO: display mean travel time
    print("The total travel time is {} minutes per trip.".format(round(df['Trip Duration'].mean(),2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    user_types = df['User Type'].value_counts()
    for user in user_types.index:
        print("The count of user type {} is {}.".format(user,user_types[user]))

    try:
        user_gender = df['Gender'].value_counts()
        for user in user_gender.index:
            print("The count of {} users is {}.".format(user,user_gender[user]))



    # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year of birth is {}\nThe most recent year of birth is {}\nThe most common year of birth year is {}".format(int(min(df['Birth Year'])),
        int(max(df['Birth Year'])),int(df['Birth Year'].mode()[0])))

    except KeyError:
        print ('No Gender information for this city.')
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_raw_data(df):
    ''' A function to display 5 lines of raw data upon the request of the user.
    Args:
        df: Data frame of  filtered data.
    Returns:
        none.
        '''

    i=0
    raw_data = input("Would you like to view raw data? [yes/no] ").lower()

    while True:
        if raw_data in ['no','n']:
            print("Thank you for reviewing raw data")
            break
        elif raw_data in ['yes','y']:
            row_index = df.index[i:i+5]
            pd.set_option('display.max_columns',200)
            print(df.loc[row_index,:])
            raw_data = input("Would you like to view more raw data? [yes/no] ").lower()
            i += 5
        else:
            print("Please enter a valid answer to view raw data: ")
            raw_data = input("Would you like to view raw data? [yes/no] ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter [yes/no] ')
        while True:
            if restart.lower() in ['no','n']:
                exit()
            elif restart.lower() in ['yes','y']:
                main()
            else:
                print("Please enter a valid answer to restart or to end: ")
                restart = input("Would you like to restart? Enter [yes/no] ").lower()



if __name__ == "__main__":
	main()
