# MapleTracker
#### Video Demo:  [HERE](https://www.youtube.com/watch?v=GdRTVsSfu-o)
#### Description:
This project is a specialized web application designed for tracking daily and weekly quests in the popular game MapleStory. It allows users to create personalized accounts, log in, and manage their quest progress with ease, ensuring they never miss crucial daily or weekly quests due to server time resets. Here’s a more detailed breakdown of the features, functionality, and structure of the app:

1. Overview of the App's Purpose
The MapleStory quest tracker is intended to help players stay organized with the game's recurring quests, which refresh either daily or weekly. In MapleStory, timing is key as quests reset at specific intervals aligned with server time. Missing a reset window could mean losing valuable rewards or progress, so this app provides timely reminders and keeps users updated on what they need to complete before time runs out.

With this app, players can:

- Track daily and weekly quests with separate sections.
- Check current server time to align their quest completion effectively.
- Input, delete, and mark quests as completed directly in the web app, creating an organized and easy-to-manage task list.

2. Account Management and Authentication
To ensure data privacy and personalize the tracking experience, the app includes a user account system with secure login and registration functionalities:

Registration: New users create a unique account by choosing a username and password. During registration:

- Users are required to confirm their password to avoid errors.
- If a user tries to register with an existing username, an error message is displayed, prompting them to choose a different username.
- Once registered, each user's data is saved in an SQLite database, linking their quests to their specific account.
-Login: Users are prompted to log in each time they visit the app, with the default landing page set to the login page ("/login").

Upon entering their credentials, the app checks if the username exists and whether the password matches.
If successful, they are directed to the main tracking page; otherwise, an error is shown.
By requiring login, the app keeps each user's quest list separate and secure, ensuring that only they can view or modify their tracked quests.

3. Task Management: Daily and Weekly Quest Tracking
The app has two main sections dedicated to tracking different types of quests:

Daily Quests Section: Here, players can list quests they plan to complete within the current day. This section is designed to reset at midnight server time, allowing users to know exactly how much time remains until their daily quests are no longer available.

Weekly Quests Section: Weekly quests have a slightly longer window, resetting at midnight every Wednesday (based on server time). This allows users to plan their tasks for the entire week while being mindful of the reset deadline.

Timer Displays: Above each section (daily and weekly), a countdown timer shows the remaining time until the reset. This feature is crucial, as it visually indicates the urgency for completing tasks and helps players prioritize their quests effectively.

Within each section, users can:

- Add New Quests: Input the quests they wish to complete for the day or week.
- Mark Quests as Completed: Check off quests as they complete them, making it easy to see what remains.
- Delete Quests: Remove any quests they no longer plan to pursue, keeping their list organized and clutter-free.

4. Back-End Development with Flask and SQLite
The app is powered by a Python back-end using Flask, a lightweight and flexible web framework, and SQLite, a simple and reliable database solution:

Routes and Views: In the app.py file, all routes are defined to serve different HTML files and handle requests.

For example, routes exist for /login, /register, and /tracker to direct users to the corresponding pages.
Each route is connected to the appropriate HTML files, facilitating seamless navigation across the app.
Database Structure:

- Accounts Table: Stores user information, including usernames and passwords.
- Tasks Table: Stores tasks linked to specific users, separating daily and weekly tasks to enable precise tracking.
- The database is designed to maintain data consistency and enable easy querying, allowing users to have a smooth experience when adding, viewing, or managing their tasks.

5. Front-End Design with HTML, CSS, and Bootstrap
The app’s front end is constructed with HTML and styled with CSS, with the layout.html file providing the base structure for consistent navigation and style across all pages:

Navigation Bar: The navbar at the top adjusts based on the user's login status. If the user is logged in, they’ll see options to navigate to the tracker or log out, while logged-out users will see options to log in or register.

Login and Registration Forms:

- The login form includes fields for entering a username and password.
- The registration form contains fields for creating a username, setting a password, and confirming the password, adding security and validation to the registration process.
Main Tracker Page (/tracker):

The main page after login is where users manage their quests. The layout is divided into sections for daily and weekly quests, each featuring input fields, buttons for adding tasks, and checkboxes for marking tasks as complete.

Styling with styles.css:

Custom CSS styling enhances the visual appeal and usability of the app. Styling includes the positioning of elements, color schemes, fonts, and button styles to make the app intuitive and pleasant to use.




