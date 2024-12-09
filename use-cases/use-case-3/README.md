# Foodie Finder
---
## Description
FoodieFinder helps users discover local restaurants and food trucks, view menus, and leave reviews.
---
## Getting Started
To get started with Foodie Finder, follow these steps:
- Clone the repository
- Install dependencies using npm install
- Start the server using npm start
---
## Scripts
The following scripts are available:
| Script | Description | Command |
| --- | --- | --- |
| start | Start the server | npm run start |
| dev | Start the server with nodemon | npm run dev |
| test | Run tests | npm run test |
| build | Build the project | npm run build |
| serve | Serve the project | npm run serve |
| lint | Lint the code | npm run lint |
| prettify | Format the code | npm run prettify |
| db:migrate | Migrate the database | npm run db:migrate |
| db:seed | Seed the database | npm run db:seed |
| clean | Clean the dist folder | npm run clean |
| check-types | Check types with tsc | npm run check-types |
---
## Dependencies
| Package | Version |
| --- | --- |
| express | >=4.18.2 |
| sequelize | >=6.33.0 |
| pg | >=8.11.0 |
| cors | >=2.8.5 |
| dotenv | >=16.0.3 |
| axios | >=1.6.0 |
| jsonwebtoken | >=9.1.1 |
| multer | >=1.4.5-lts.1 |
| sharp | >=0.32.0 |
| uuid | >=9.0.0 |
---
## Author
Liam Chen
[Liam Chen](https://www.foodiefinder.io/team/liam)
---
## License
Foodie Finder is licensed under the Apache License, Version 2.0.
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
---
## Repository
[Foodie Finder](https://github.com/foodiefinder/foodie-finder)
[Report Issues](https://github.com/foodiefinder/foodie-finder/issues)
[Homepage](https://www.foodiefinder.io)
---
## Keywords
- food
- restaurants
- reviews
- discovery
- web app
---
## Engines
| Node | NPM |
| --- | --- |
| >=16.0.0 | >=8.0.0 |
---
## Config
| Port | DB Host | DB Port |
| --- | --- | --- |
| 3000 | localhost | 5432 |
---
## Workspaces
- api
- frontend
- shared
---
## Type
module
---
## Exports
```
{
    ".": {
        "import": "./dist/index.mjs",
        "require": "./dist/index.cjs"
    },
    "./routes": {
        "import": "./dist/routes/index.mjs",
        "require": "./dist/routes/index.cjs"
    }
}
```
---
## Bugs
[Report Issues](https://github.com/foodiefinder/foodie-finder/issues)
---
