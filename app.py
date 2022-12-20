import api_actions
import db_actions


def main():
    """
    - Gets s&p500 symbols, writes to company relation
    - Gets s&p500 symbol history, writes to values relation (in progress)

    Parameters
    ----------

    Returns
    -------

    """
    # get symbols and basic company data data from web source (wikipedia)
    symbols, data = api_actions.get_company()

    # write symbols to company table in postgres
    db_actions.write_company(data)

    # get values with symbols 
    # api_actions.get_values(symbols)

main()
