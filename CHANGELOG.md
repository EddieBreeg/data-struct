# Changelog

### 1.2.0

None (or empty) objects are no longer deleted automatically when you modify a Struct object.

### 1.1.0

The _Struct_ constructor now accepts any type of object! If the given object is not a list nor a dict, it will be deserialized.\
See the README for more details.

#### 1.0.1

Changed a bug such that when a list in the Struct object became empty, it was not deleted as it should

## 1.0.0

Project renamed to **data-struct**

### 0.2.0

The function argument of the sorted and sort methods now defaults to `lambda x:x`.
This argument now works even if the path argument is set to `None`.

### 0.1.0

Initial release of the _data-struct_ library!