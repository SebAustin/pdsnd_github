"""
Bikeshare Data Analysis Application

This module provides an interactive command-line application for analyzing
bikeshare data from three major US cities: Chicago, New York City, and Washington.

The application allows users to filter data by city, month, and day of week,
then displays various statistics about bikeshare usage patterns.

Author: Sebastien Henry
Date: 2024
"""

import time
import pandas as pd
import numpy as np

# Dictionary mapping city names to their corresponding CSV data files
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    This function prompts the user for three pieces of information to filter
    the bikeshare data. All inputs are validated and case-insensitive.

    Returns:
        tuple: A tuple containing three strings:
            - city (str): Name of the city to analyze ('chicago', 'new york city', or 'washington')
            - month (str): Name of the month to filter by ('january' through 'june'), or 'all' for no filter
            - day (str): Name of the day of week to filter by ('monday' through 'sunday'), or 'all' for no filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city - validate against available cities
    # Input is converted to lowercase for case-insensitive comparison
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('\nWhich city would you like to explore? (Chicago, New York City, Washington)\n').strip().lower()
        if city in cities:
            break
        else:
            print('Invalid input. Please enter one of: Chicago, New York City, or Washington.')
    
    # Get user input for month - only data for January through June is available
    # User can also select 'all' to include all months without filtering
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nWhich month would you like to filter by? (all, January, February, March, April, May, June)\n').strip().lower()
        if month in months:
            break
        else:
            print('Invalid input. Please enter one of: all, January, February, March, April, May, or June.')
    
    # Get user input for day of week - validate against all days
    # User can also select 'all' to include all days without filtering
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('\nWhich day of the week would you like to filter by? (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)\n').strip().lower()
        if day in days:
            break
        else:
            print('Invalid input. Please enter one of: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    This function reads the CSV file for the selected city, converts the Start Time
    to datetime format, extracts temporal features, and applies user-specified filters.

    Args:
        city (str): Name of the city to analyze ('chicago', 'new york city', or 'washington')
        month (str): Name of the month to filter by ('january' through 'june'), or 'all' for no filter
        day (str): Name of the day of week to filter by ('monday' through 'sunday'), or 'all' for no filter
        
    Returns:
        pandas.DataFrame: DataFrame containing city data filtered by month and day,
                         with additional columns for 'month' and 'day_of_week'
    """
    # Load the CSV data file for the selected city into a pandas DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column from string to datetime object for time-based operations
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month (as integer 1-12) and day of week (as string name) from Start Time
    # These new columns will be used for filtering and statistical analysis
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Apply month filter if user didn't select 'all'
    if month != 'all':
        # Convert month name to integer (1-6) by finding its index in the months list
        # Adding 1 because list indices start at 0 but months start at 1
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # Filter the DataFrame to only include rows matching the selected month
        df = df[df['month'] == month]

    # Apply day of week filter if user didn't select 'all'
    if day != 'all':
        # Filter the DataFrame to only include rows matching the selected day
        # Using .title() to match the capitalized format from dt.day_name()
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Calculates and displays the most common month, day of week, and hour
    for bikeshare trips in the filtered dataset.
    
    Args:
        df (pandas.DataFrame): DataFrame containing filtered bikeshare data
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculate and display the most common month using mode (most frequent value)
    # Subtracting 1 to convert from month number (1-6) to list index (0-5)
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most Common Month:', months[common_month - 1])

    # Calculate and display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day)

    # Extract hour from Start Time and find the most common start hour (0-23 format)
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Calculates and displays the most frequently used start station, end station,
    and the most common trip (start-end station combination).
    
    Args:
        df (pandas.DataFrame): DataFrame containing filtered bikeshare data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find and display the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # Find and display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # Create a combined trip column by concatenating start and end stations
    # Then find the most frequent trip combination
    df['trip'] = df['Start Station'] + ' --> ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print('Most Common Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Calculates the sum and mean of all trip durations in the filtered dataset,
    converting the results from seconds to a more readable format.
    
    Args:
        df (pandas.DataFrame): DataFrame containing filtered bikeshare data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time across all trips (in seconds)
    total_travel_time = df['Trip Duration'].sum()
    # Convert total seconds to hours, minutes, and seconds for better readability
    hours = int(total_travel_time // 3600)
    minutes = int((total_travel_time % 3600) // 60)
    seconds = int(total_travel_time % 60)
    print('Total Travel Time: {} hours, {} minutes, {} seconds'.format(hours, minutes, seconds))

    # Calculate average (mean) travel time per trip (in seconds)
    mean_travel_time = df['Trip Duration'].mean()
    # Convert average seconds to minutes and seconds for better readability
    mean_minutes = int(mean_travel_time // 60)
    mean_seconds = int(mean_travel_time % 60)
    print('Average Travel Time: {} minutes, {} seconds'.format(mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Calculates and displays user type distribution, gender breakdown (if available),
    and birth year statistics (if available). Note that Gender and Birth Year data
    are not available for Washington DC.
    
    Args:
        df (pandas.DataFrame): DataFrame containing filtered bikeshare data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate and display the count of each user type (e.g., Subscriber, Customer)
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display gender distribution if the data is available
    # Washington DC data does not include gender information
    try:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Breakdown:\n', gender_counts)
    except KeyError:
        print('\nGender data is not available for this city.')

    # Display birth year statistics if the data is available
    # Washington DC data does not include birth year information
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
    """
    Displays raw data 5 rows at a time upon user request.
    
    This function provides an interactive way for users to view the raw data
    from the filtered dataset. It displays 5 rows at a time and continues
    to show more rows as long as the user confirms.
    
    Args:
        df (pandas.DataFrame): DataFrame containing the filtered city data
    """
    row_index = 0
    while True:
        # Prompt user to view raw data
        view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n').strip().lower()
        if view_data != 'yes':
            break
        
        # Check if there are more rows available to display
        if row_index >= len(df):
            print('\nNo more raw data to display.')
            break
        
        # Display the next 5 rows of data using iloc for integer-location based indexing
        print('\n', df.iloc[row_index:row_index + 5])
        row_index += 5


def main():
    """
    Main function to run the bikeshare data analysis application.
    
    This function orchestrates the entire application flow:
    1. Gets user filters (city, month, day)
    2. Loads and filters the data
    3. Displays various statistics
    4. Offers to display raw data
    5. Allows user to restart with different filters or exit
    """
    while True:
        # Get user input for filters
        city, month, day = get_filters()
        
        # Load and filter the data based on user selections
        df = load_data(city, month, day)

        # Display all statistical analyses
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Offer to display raw data if user is interested
        display_raw_data(df)

        # Ask if user wants to restart with different filters
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    # Entry point: run main function when script is executed directly
    main()
