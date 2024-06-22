import { Nav } from "react-bootstrap";
import { NavDropdown } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export interface MenuItemProps {
  name: string;
  link: string;
}

export interface CategoryProps {
  name: string;
  links: Array<MenuItemProps>;
}

export interface CorpMenuProps extends Partial<HTMLElement> {
  isLoading?: boolean;
  data?: Array<CategoryProps> | null;
  error?: boolean;
}

const CorpMenu = (props: CorpMenuProps) => {
  console.log(props);
  return (
    <>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/glance`}>
          <Nav.Link key="Glance">Overview</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/structures`}>
          <Nav.Link key="Structures">Structures</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/wallets`}>
          <Nav.Link key="Wallets">Wallets</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/assetgroup`}>
          <Nav.Link key="assetgroup">Asset Overview</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/assetlist`}>
          <Nav.Link key="assetlist">Asset List</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <Nav.Item>
        <LinkContainer to={`/audit/r_beta/corp/pocos`}>
          <Nav.Link key="pocos">Pocos</Nav.Link>
        </LinkContainer>
      </Nav.Item>
      <NavDropdown title="Dashboards">
        <LinkContainer to={`/audit/r_beta/corp/bridges`}>
          <Nav.Link key="bridges">Bridges</Nav.Link>
        </LinkContainer>
        <LinkContainer to={`/audit/r_beta/corp/sov`}>
          <Nav.Link key="bridges">Sov Upgrades</Nav.Link>
        </LinkContainer>
      </NavDropdown>

      {/* {data &&
        data.map((cat: CategoryProps) => {
          return (
            <NavDropdown id={cat.name} title={cat.name} key={cat.name}>
              {cat.links.map((link: MenuItemProps) => {
                return (
                  <LinkContainer to={`/audit/r/${characterID}/${link.link}`}>
                    <NavDropdown.Item id={link.name} key={link.name}>
                      {link.name}
                    </NavDropdown.Item>
                  </LinkContainer>
                );
              })}
            </NavDropdown>
          );
        })} */}
    </>
  );
};

export default CorpMenu;
