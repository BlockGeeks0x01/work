-- --------------------------------------------------------------------------------
-- Routine DDL
-- Note: comments before and after the routine body will not be stored by the server
-- --------------------------------------------------------------------------------
DELIMITER $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `show_table_info`(in _schema varchar(30), in _table varchar(30), IN _showrowno BOOL)
BEGIN

set @rowNo = 0;

IF _showrowno then

select (@rowNo := @rowNo + 1) as rowno, col.column_name as name, col.data_type as type, concat(k.REFERENCED_TABLE_NAME,'(',k.REFERENCED_COLUMN_NAME ,')') as 'realation_table' ,col.column_comment as comment
from  information_schema.columns col
left outer join information_schema.key_column_usage k on k.table_name = col.table_name and k.table_schema = col.table_schema and k.column_name = col.column_name
where col.table_name = _table and col.table_schema = _schema;

else

select col.column_name as name, col.data_type as type, concat(k.REFERENCED_TABLE_NAME,'(',k.REFERENCED_COLUMN_NAME ,')') as 'realation_table' ,col.column_comment as comment
from  information_schema.columns col
left outer join information_schema.key_column_usage k on k.table_name = col.table_name and k.table_schema = col.table_schema and k.column_name = col.column_name
where col.table_name = _table and col.table_schema = _schema;

end if;

END