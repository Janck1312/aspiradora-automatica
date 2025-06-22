from components.common.TableComponent.ColumnParamsInterface import ColumnParamsInterface
from components.common.TableComponent.ConfigInterface import ConfigInterface
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class TableComponent():
    """TABLE COMPONENT USED TO SHOW RECORDS IN A TABLE WITH PAGINATION"""

    def setColumns(self, columns) -> None:
        """Set&config columns of dataTable EXAMPLE
            [
                ("col_header", dp(60), self.sort_on_signal)
            ]
        """ 
        self.columns = columns

    def setData(self, data:any) -> None:
        """set data of dataTable EXAMPLE
            [
                ( "data first column" )
            ]
        """
        self.data = data if data is not None else []

    def initDataTable(self, config: ConfigInterface=None):
        """CONFIG DataTable EXAMPLE
            config = ConfigInterface()
            config.check = True
            config.size_hint = (0.7, 0.6),
            config.use_pagination = True

            TableComponent().initDataTable(config)
        """
        return MDDataTable(
            size_hint=config.size_hint or (1, .5),
            use_pagination=config.use_pagination or False,
            check=config.check or False,
            column_data=self.columns,
            row_data=self.data,
        )


