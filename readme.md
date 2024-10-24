Server:
~/dbfiles/
~/*

run: docker compose -f docker-compose.dev.yml up --build -d

### Backend
If after building the application, the backed container does not start, you need to remove the 'migrations' folders


### Connecting to PostgreSQL server
* On host go to `localhost:5420`
* Right click Servers, located on the left side of browser window, then select Register, server
* Fill in Name field with whatever name you like
* Go to Connection section
  * Host name/address: `host.docker.internal`
  * Port: `5432`
  * Maintenance database: `student`
  * Username: `student`
  * Password: `student`


# Frontend
create file Frontend/.env.local with these lines in it:
`NEXTAUTH_SECRET=[secret key]`
`NEXTAUTH_URL=http://localhost:3000/`
And to get secret key run this command in ubuntu: `openssl rand -base64 32` 

### Gateway
* Role:
  * 1 - Admin
  * 2 - Employee
  * 3 - User

#### Config
* /login 
  * @Post
  * @Get
* /logout
  * @Post
  * @Get
* /admin
  * @Post
  * @Get
  * @Patch
  * @Delete
* /employee
  * @Post
  * @Get
  * @Patch
  * @Delete
* /user
  * @Post
  * @Get
  * @Patch
  * @Delete