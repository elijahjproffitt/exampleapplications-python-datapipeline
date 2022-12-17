import api_actions
import db_actions


def main():
    """
    - Gets s&p500 tickers, writes to company relation
    - Gets s&p500 ticker history, writes to values relation (in progress)

    Parameters
    ----------

    Returns
    -------

    """
    # get symbols and basic company data data from wikipedia
    symbols, data = api_actions.get_company()

    # write symbols to db
    db_actions.write_company(data)

    # get values with tickers 
    api_actions.get_values(symbols)

main()