
## __CRUD: Restaurant Booking__

Welcome to Restoran, your go-to platform for hassle-free reservation management. If you have a restaurant and you want to provide a better service to your customers we streamlines the reservation process. Users can create accounts, log in, and enjoy the convenience of managing their reservations effortlessly.

![Mockup](readme/all-devices-white.png "Website preview at different resolutions")

[Live link to website](https://crud-p4-6d939b734527.herokuapp.com/)
## __Tech Stack__

<img height="50" src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png"> **VS Code**
<img height="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png"> **Python**
<img height="50" src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4"> **Django**
<img height="50" src="https://user-images.githubusercontent.com/25181517/117364277-fc4eb280-aebd-11eb-8769-a3583c6a2037.png"> **Git**
<img height="50" src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png"> **HTML**
<img height="50" src="https://user-images.githubusercontent.com/25181517/183898674-75a4a1b1-f960-4ea9-abcb-637170a00a75.png"> **CSS**
<img height="50" src="https://user-images.githubusercontent.com/25181517/117447155-6a868a00-af3d-11eb-9cfe-245df15c9f3f.png"> **JavaScript**
<img height="50" src="https://user-images.githubusercontent.com/25181517/183898054-b3d693d4-dafb-4808-a509-bab54cf5de34.png"> **Bootstrap**
<img height="50" src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png"> **PostgreSQL**

## UX & Design

### Target Audience

The target audience for the reservation management web application, includes individuals and businesses involved in scheduling and managing reservations. Here's a breakdown of the target audience:

**Individual Users:**

Diners: People who want to book tables at restaurants for personal or group dining experiences.

**Business Owners:**

Restaurants and Cafes: Businesses that offer dining services and want a streamlined system for managing table reservations.

**Administrators and Superusers:**

Administrators: Individuals responsible for overseeing and managing the entire reservation system, ensuring its smooth operation.

Superusers: Users with elevated privileges who can access and manage all reservations, useful for system administrators or venue owners.


### User Stories


- As a new user, I want to be able to register for a ReserveMeNow account.
- As a user, I want the registration process to be simple and secure.
- As a registered user, I want to log in to my ReserveMeNow account.
- As a user, I want my account to be protected with secure authentication.
- As a user, I want to create a new reservation for a specific date and time.
- As a user, I want the ability to specify the number of people for my reservation.
- As a user, I want to view a list of my upcoming reservations.
- As a user, I want details such as date, time, and venue displayed for each reservation.
- As a user, I want to be able to update the details of my existing reservations.
- As a user, I want the option to change the date, time, or the number of people for a reservation.
- As a user, I want the ability to cancel a reservation when necessary.
- As a user, I want to include special requests or notes when making a reservation.
- As a user, I want to view any special requests associated with my reservations.

- As a superuser, I want to have access to view and manage all reservations.
- As a superuser, I want the capability to edit or delete any reservation.


### __Color Scheme__

I used [Coolors.co](https://coolors.co/) to keep a control on the color scheme selected.
<kbd>
<img height="400" src="https://github.com/giankpetrov/CRUD-P4/blob/main/readme/colorcode.png">
</kbd>

### __Contrast Checker__

I used [Coolors.co](https://coolors.co/) contrast checker tool having a super result of 17.83.
<kbd>
<img height="400" src="https://github.com/giankpetrov/CRUD-P4/blob/main/readme/contrastchecker.PNG">
</kbd>

### __Future development__

- __Email Service__
    - This will allow send an email to the customer with the reservation details.

- __Newsletter Registration__
    - This will allow customer to get the latest information and deals from the restaurant or bar.

## Deployment

The live deployed application can be found deployed on Heroky [Here](https://crud-p4-6d939b734527.herokuapp.com/).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: tribe).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | insert your own Cloudinary API key here |
| `DATABASE_URL` | insert your own ElephantSQL database URL here |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | this can be any random secret key |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!
## __Credits__

### Code

- Starting idea for page functionality from [John Elder.](https://www.linkedin.com/in/john-elder-493a3155/)
- Project reviewed for README file structure [Adam Gilroy.](https://github.com/adamgilroy22/tribe)

### Design

- Favincon made with [Favicon.io](https://favicon.io/)
- Color palette from [Coolors](https://coolors.co/)
- Font from [Google Fonts](https://fonts.google.com/)
- Concept design and Theme [HTML Codex.](https://htmlcodex.com/) Distributed by[ThemeWagon.](https://themewagon.com/)
- Tech Stack Icons [github.com/Marwin1991](https://github.com/marwin1991/profile-technology-icons)

Namaste ☸
