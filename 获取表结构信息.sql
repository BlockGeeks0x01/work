DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `show_table_info`(in _schema varchar(30), in _table varchar(30))
BEGIN

select col.column_name as name, col.data_type as type, concat(k.REFERENCED_TABLE_NAME,'(',k.REFERENCED_COLUMN_NAME ,')') as 'realation_table' ,col.column_comment as comment
from  information_schema.columns col
left outer join information_schema.key_column_usage k on k.table_name = col.table_name and k.table_schema = col.table_schema and k.column_name = col.column_name
where col.table_name = _table and col.table_schema = _schema;

END$$
DELIMITER ;
