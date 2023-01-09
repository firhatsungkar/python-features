Data Classes
======

Python data classes are - as you'd expect - in particular suitable to model classes that represent data, and as such they offer easy mechanisms to initialize, print, order, sort and compare data.

> `Note:` that although I'm using a sort_index attribute, strictly speaking that's not needed in this case, because a data class uses a tuple of its attributes in the class definition as the default for sorting. I'm not a fan of this kind of hidden behavior, so I prefer to do it explicitly (using something that is called sort_index in this case). Another advantage of using a separate field, is that you can do more complicated ordering, using for example a weighted combination of age and strength.