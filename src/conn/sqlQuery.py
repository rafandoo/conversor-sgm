import logging

class QueryMaker():

    def __init__(self, sysout=True):
        self.__sysout = sysout

    def simple(self, table, order, cols='*', cmd='SELECT', filter=None):
        """
        Generate a SQL query string using the given table name, column names, command, and filter.

        :param table: str - The name of the table to query.
        :param order: str - The parameter to order the query by. 
        :param cols: str - The columns to include in the query. Default is '*'.
        :param cmd: str - The command to use in the query. Default is 'SELECT'.
        :param filter: str - The filter to apply to the query. Default is None, meaning no filter will be applied.

        :return: str - The generated SQL query string.
        """
        query = cmd + ' ' + cols + ' FROM ' + table
        if filter:
            query += (' WHERE ' + filter)
        query += (' ORDER BY ' + order)
        if self.__sysout:
            logging.debug(query)
        return query

    def leftJoin(self, table1, table2, param1, param2, order, cols='*', cmd='SELECT', filter=None):
        """
        Generate a SQL query string using the given table names, column names, command, and filter.

        :param table1: str - The name of the first table to join.
        :param table2: str - The name of the second table to join.
        :param param1: str - The parameter to find in the first table.
        :param param2: str - The parameter to find in the second table.
        :param order: str - The parameter to order the query by.
        :param cols: str - The columns to include in the query. Default is '*'.
        :param cmd: str - The command to use in the query. Default is 'SELECT'.
        :param filter: str - The filter to apply to the query. Default is None, meaning no filter will be applied.

        :return: str - The generated SQL query string.
        """
        query = cmd + ' ' + cols + ' FROM ' + table1 + ' LEFT JOIN ' + table2 + \
            ' ON (' + table1 + '.' + param1 + \
            ' = ' + table2 + '.' + param2 + ')'
        if filter:
            query += ' WHERE ' + filter
        query += ' ORDER BY ' + order
        if self.__sysout:
            logging.debug(query)
        return query

    def fullOuterJoin(self, table1, table2, param1, param2, order, cols='*', cmd='SELECT', filter=None):
        """
        Executes a FULL OUTER JOIN SQL query on two tables provided and returns the resulting query.

        :param table1: str - The name of the first table to join.
        :param table2: str - The name of the second table to join.
        :param param1: str - The first parameter to use for the join condition.
        :param param2: str - The second parameter to use for the join condition.
        :param order: str - The column to use for ordering the query results.
        :param cols: str - The columns to select from the resulting query. Defaults to '*'.
        :param cmd: str - The SQL command to execute. Defaults to 'SELECT'.
        :param filter: str - The filter to apply to the query. Defaults to None.

        :return: str - The resulting FULL OUTER JOIN query as a string.
        """
        query = cmd + ' ' + cols + ' FROM ' + table1 + ' FULL OUTER JOIN ' + table2 + \
            ' ON (' + table1 + '.' + param1 + \
            ' = ' + table2 + '.' + param2 + ')'
        if filter:
            query += ' WHERE ' + filter
        query += ' ORDER BY ' + order
        if self.__sysout:
            logging.debug(query)
        return query

    def doubleLeftJoin(self, table1, table2, table3, param1, param2, param3, order, cols='*', cmd='SELECT', filter=None):
        """
        Performs a left join on three tables given their names and parameters.

        :param table1: str - The name of the first table to join.
        :param table2: str - The name of the second table to join.
        :param table3: str - The name of the third table to join.
        :param param1: str - The parameter used to join table1 and table2.
        :param param2: str - The parameter used to join table2.
        :param param3: str - The parameter used to join table1 and table3.
        :param order: str - The column to order the resulting query by.
        :param cols: str - The columns to include in the query (default: '*').
        :param cmd: str - The SQL command to use (default: 'SELECT').
        :param filter: str - The filter to apply to the query (default: None).

        :return: str - The resulting SQL query as a string.
        """
        query = cmd + ' ' + cols + ' FROM ' + table1 + ' LEFT JOIN ' + table2 + \
            ' ON (' + table1 + '.' + param1 + \
            ' = ' + table2 + '.' + param2 + ')'
        query += ' LEFT JOIN ' + table3 + \
            ' ON (' + table1 + '.' + param1 + \
            ' = ' + table3 + '.' + param3 + ')'
        if filter:
            query += ' WHERE ' + filter
        query += ' ORDER BY ' + order
        if self.__sysout:
            logging.debug(query)
        return query
