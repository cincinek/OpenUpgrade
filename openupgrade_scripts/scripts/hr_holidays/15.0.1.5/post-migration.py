from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env.cr, "hr_holidays", "15.0.1.5/noupdate_changes.xml")
