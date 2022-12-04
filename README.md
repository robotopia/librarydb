# LibraryDB
A simple home library database

This document contains the specifications of a simple home library database.
The purpose of the database is not to provide all possible metadata of the books themselves, but rather to keep track of where books are in the house.
It serves as a kind of substitute for book cataloguing systems (e.g. Dewey Decimal System) for the commonly occuring situation where the available storage space is not amenable to strict ordering of books.

## Specification

### "Book" Object

A Book object consists of:

| Field | Type | Required | Description |
| :---: | :--: | :------: | :---------- |
| title | string | Y | The title of a book |
| isbn | integer | N | The book's ISBN |
| storage | Storage | N | The storage container where the book normally resides |
| shelf | integer | N | The shelf number, if the storage container is a bookcase (1 = top, 2 = second from the top, etc.) |
| authors | List of Author objects | N | The author(s) of the book |

### "Author" Object

An Author object consists of:

| Field | Type | Required | Description |
| :---: | :--: | :------: | :---------- |
| surname | string | Y | The author's surname |
| givenname | string | N | The author's given name(s) (or initials) |

### "Room" Object

A Room object consists of:

| Field | Type | Required | Description |
| :---: | :--: | :------: | :---------- |
| name | string | Y | A short name for the room (e.g. "garage") |
| location | string | N | A description of the room's location that can be used to unambiguously identify where it is |

### "Storage" Object

A Storage object represents a generic storage container (e.g. bookcase, box). It consists of:

| Field | Type | Required | Description |
| :---: | :--: | :------: | :---------- |
| name | string | Y | A name for the storage container |
| room | Room | N | Which room the storage container is in |
| type | string | N | The storage container type (e.g. 'bookcase', 'box')
| description | string | N | A description of the storage container that can uniquely identify it |

### "Version" Object

This specification's versioning is handled using the standard `MAJOR.MINOR.PATCH` framework, with the `MAJOR` and `MINOR` version numbers implemented as git tags, and `PATCH` being the number of commits since the most recent tag.
Any implementation of this specification must also include the means to track which version of the specification was used at the time of implementation, and optionally which range of versions the implementation is compatible with.

| Field | Type | Required | Description |
| :---: | :--: | :------: | :---------- |
| created | string | Y | Version number used to create the database, in the format `MAJOR.MINOR.PATCH` |
| min_version | string | N | Minimum version compatible with this database |
| max_version | string | N | Maximum version compatible with this database |

## Implementations

- **Django**: See the [django_app](django_app) folder.
