import time
import pandas as pd
import numpy as np

# Constants for data files and valid filter options
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
VALID_DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June']


def get_user_input(prompt, valid_options, error_message):
    """Helper function to get and validate user input."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(error_message)


def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city using helper function
    city = get_user_input(
        '\nWhich city would you like to explore? (Chicago, New York City, Washington)\n',
        VALID_CITIES,
        'Invalid input. Please enter one of: Chicago, New York City, or Washington.'
    )
    
    # Get user input for month using helper function
    month = get_user_input(
        '\nWhich month would you like to filter by? (all, January, February, March, April, May, June)\n',
        VALID_MONTHS,
        'Invalid input. Please enter one of: all, January, February, March, April, May, or June.'
    )
    
    # Get user input for day of week using helper function
    day = get_user_input(
        '\nWhich day of the week would you like to filter by? (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)\n',
        VALID_DAYS,
        'Invalid input. Please enter one of: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.'
    )

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        month_num = VALID_MONTHS.index(month)
        df = df[df['month'] == month_num]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print('Most Common Month:', MONTH_NAMES[common_month - 1])

    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day)

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    df['trip'] = df['Start Station'] + ' --> ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most Common Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    hours = int(total_travel_time // 3600)
    minutes = int((total_travel_time % 3600) // 60)
    seconds = int(total_travel_time % 60)
    print('Total Travel Time: {} hours, {} minutes, {} seconds'.format(hours, minutes, seconds))

    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = int(mean_travel_time // 60)
    mean_seconds = int(mean_travel_time % 60)
    print('Average Travel Time: {} minutes, {} seconds'.format(mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    try:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Breakdown:\n', gender_counts)
    except KeyError:
        print('\nGender data is not available for this city.')

    try:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nBirth Year Statistics:')
        print('  Earliest Birth Year:', earliest_birth_year)
        print('  Most Recent Birth Year:', most_recent_birth_year)
        print('  Most Common Birth Year:', most_common_birth_year)
    except KeyError:
        print('\nBirth Year data is not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""
    row_index = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n').strip().lower()
        if view_data != 'yes':
            break
        
        if row_index >= len(df):
            print('\nNo more raw data to display.')
            break
        
        print('\n', df.iloc[row_index:row_index + 5])
        row_index += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
