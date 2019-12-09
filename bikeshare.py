# Importing all neccessery libraries.
import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Enter the city you would like to analyze (Chicago, New York City or Washington)\n'))
            city = city.lower().replace(' ','_')
            if city == 'chicago' or city == 'new_york_city' or city == 'washington':
                print('\nAlright let\'s check it out!\n')
                break
            else:
                print('\n You didn\'t enter a valid city ! \n')
        except:
            print('Try again ! \n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Enter the month you would like to filter by (all, january, february, ... , june)\n'))
            month = month.lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                print('\nGreat!\n')
                break
            else:
                print('\n You didn\'t enter a valid month ! \n')
        except:
            print('Try again ! \n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Enter the day you would like to filter by (all, monday, tuesday, ... sunday)\n'))
            day = day.lower()
            if day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'all':
                break
            else:
                print('\n You didn\'t enter a valid day ! \n')
        except:
            print('Try again ! \n')

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
    # load data file into a dataframe
    df = pd.read_csv('{}.csv'.format(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df,city,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #global month,city,day
    # TO DO: display the most common month
    if month == 'all':
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = months[popular_month - 1].title()
        print('\nMost popular month is: ',popular_month)

    # TO DO: display the most common day of week
    if day == 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        popular_day = df['day_of_week'].mode()[0]
        print('\nMost popular day of week is: ',popular_day)

    # TO DO: display the most common start hour
    df['st_hour'] = df['Start Time'].dt.hour
    popular_st_hour = df['st_hour'].mode()[0]
    print('\nMost common start hour is: ',popular_st_hour)

    # Additional: display the most common end hour
    df['end_hour'] = df['End Time'].dt.hour
    popular_end_hour = df['end_hour'].mode()[0]
    print('\nMost common end hour is: ',popular_end_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_st_station = df['Start Station'].mode()[0]
    print('\n Most commonly used start station is: \n',pop_st_station)

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('\n Most commonly used end station is: \n',pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    pop_st_to_end_Station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\n Most frequent combination of start station and end station trip is: \n',pop_st_to_end_Station)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_duration = df['Trip Duration'].sum()

    # Converting the time from seconds to [hour,min,sec] fro better realization
    seconds = tot_duration
    hour = seconds / 3600
    seconds %= 3600
    minutes = seconds / 60
    seconds %= 60
    print('\nTotal travel time is:\n%1d hours, %2d minutes and %2d seconds '%(hour,minutes,seconds))


    # TO DO: display mean travel time
    avg_duration = df['Trip Duration'].mean()

    # Converting the time from seconds to [hour,min,sec] fro better realization
    seconds = avg_duration
    hour = seconds / 3600
    seconds %= 3600
    minutes = seconds / 60
    seconds %= 60
    print('\nMean travel time is:\n%1d hours, %2d minutes and %2d seconds '%(hour,minutes,seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('\n{}\n'.format(user_types))

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('\n{}\n'.format(gender_count))
    else:
        print('\nSorry, there is no data related to gender of users\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        dob_min = int(df['Birth Year'].min())
        dob_max = int(df['Birth Year'].max())
        dob_commen = int(df['Birth Year'].mode()[0])
        print('\nEarlies birth year is: {}\nMost recent birth year is: {}\nCommen birth year is: {} '.format(dob_min,dob_max,dob_commen))
    else:
        print('\nSorry, there is no data related to the birth date of users\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city,month,day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,city,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        c = 5
        while True:
            view_data = input('\nWould you like to view lines of date? Enter yes or no.\n')
            if view_data.lower() == 'yes':
                print(df.head(c))
                c +=5

            elif view_data.lower() == 'no':
                break
            else:
                Print('\nInvalid Entry ! Try again\n')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
