### TEMPLATE METHOD EXAMPLE

In this example I built a line system with two types of line, one for normal clients and one for priotities (elder, pregnants, etc).

It uses the template design pattern in which a abstract class LineBase declares two abstract methods that the child classes must implement `generate_current_code` and `summon_client`. The abstract class also has a template method `update_line`, which calls all the method pertaining the functionallity do add a new client to the line.
